"""
AI Roadmap Generator — powered by Google Gemini (with Offline Fallback)
Generates structured, beginner-to-advanced learning roadmaps for any topic.
Falls back to curated local roadmaps when the API quota is exhausted.
"""
import json
import re
import os

# Prioritize gemini-2.0-flash (fastest) and gemini-flash-latest (most stable free tier)
_CANDIDATE_MODELS = [
    "gemini-2.0-flash",
    "gemini-flash-latest",
    "gemini-pro-latest",
]


def _search_local_roadmaps(topic: str) -> dict | None:
    """
    Search the curated roadmap collection in roadmap_content.py
    for a topic that matches the user's query.
    Returns a formatted roadmap dict or None if no match found.
    """
    try:
        from roadmap_content import ALL_ROADMAPS
    except ImportError:
        return None

    topic_lower = topic.lower().strip()
    keywords = set(topic_lower.split())

    best_match = None
    best_score = 0

    for rm in ALL_ROADMAPS:
        title_lower = rm.get("title", "").lower()
        desc_lower = rm.get("description", "").lower()
        category_lower = rm.get("category", "").lower()

        # Exact substring match in title → highest priority
        if topic_lower in title_lower:
            best_match = rm
            best_score = 100
            break

        # Keyword scoring
        score = 0
        for kw in keywords:
            if kw in title_lower:
                score += 10
            if kw in desc_lower:
                score += 3
            if kw in category_lower:
                score += 5

        if score > best_score:
            best_score = score
            best_match = rm

    if best_match and best_score >= 5:
        return _format_local_roadmap(best_match)
    return None


def _format_local_roadmap(rm: dict) -> dict:
    """Convert a roadmap_content.py entry into the same JSON shape the template expects."""
    meta = rm.get("meta_data", {})
    steps = []
    for i, s in enumerate(rm.get("steps", []), 1):
        resources = []
        for name in (s.get("resources", "") or "").split(" | "):
            name = name.strip()
            if name:
                resources.append({"name": name, "url": "#", "type": "docs"})
        steps.append({
            "step_number": i,
            "level": s.get("level", "Beginner"),
            "title": s.get("title", ""),
            "description": s.get("desc", ""),
            "resources": resources,
        })

    return {
        "title": rm.get("title", ""),
        "description": rm.get("description", ""),
        "estimated_time": meta.get("estimated_time", "Varies"),
        "difficulty": rm.get("difficulty", "intermediate").capitalize(),
        "meta_data": meta,
        "steps": steps,
        "_source": "local",  # flag so the template can show a badge
    }


def generate_roadmap(topic: str) -> dict:
    """
    Call Google Gemini to generate a structured roadmap.
    Falls back to curated local roadmaps if the API quota is exhausted (429).
    """
    api_key = os.environ.get("GEMINI_API_KEY") or _get_key_from_config()
    if not api_key:
        # No API key — try local first
        local = _search_local_roadmaps(topic)
        if local:
            return local
        raise ValueError("Gemini API key not configured and no local roadmap found. Add key to .env")

    try:
        import google.generativeai as genai
    except ImportError:
        # Library not installed — try local
        local = _search_local_roadmaps(topic)
        if local:
            return local
        raise ValueError("pip install google-generativeai")

    genai.configure(api_key=api_key)

    prompt = f"""Expert Learning Path Designer. Topic: "{topic}"
Progress: 1-3(Begin), 4-6(Inter), 7-10(Adv).
JSON ONLY:
{{
  "title": "Roadmap: {topic}",
  "description": "2-sentence overview.",
  "estimated_time": "X months",
  "difficulty": "Beginner|Intermediate|Advanced",
  "meta_data": {{ "skills": {{ "core": [] }}, "tools": [], "career_progression": [] }},
  "steps": [
    {{
      "step_number": 1, "level": "Beginner", "title": "Title", "description": "Desc.",
      "resources": [{{ "name": "Source", "url": "https://...", "type": "docs" }}]
    }}
  ]
}}
"""

    # Try faster model directly first
    last_err = None
    hit_quota = False
    for name in _CANDIDATE_MODELS:
        try:
            model = genai.GenerativeModel(name)
            response = model.generate_content(
                prompt,
                generation_config={"temperature": 0.7, "max_output_tokens": 2048}
            )
            raw = response.text.strip()
            raw = re.sub(r"^```(?:json)?\s*", "", raw, flags=re.MULTILINE)
            raw = re.sub(r"\s*```\s*$", "", raw, flags=re.MULTILINE)

            data = json.loads(raw)
            _validate_roadmap(data)
            return data

        except Exception as e:
            last_err = str(e)
            if "404" in last_err:
                continue  # Try next model
            if "429" in last_err or "quota" in last_err.lower():
                hit_quota = True
                break  # Key issue, don't spam
            continue

    # API failed — try local fallback
    local = _search_local_roadmaps(topic)
    if local:
        return local

    # Nothing worked
    if hit_quota:
        raise ValueError(
            "🚫 AI service quota exceeded. No matching roadmap found in our collection either. "
            "Please try a different topic like 'Data Science', 'Web Development', or 'Cybersecurity', "
            "or try again later."
        )
    raise ValueError(f"Could not generate roadmap. Please try again later.")


def _validate_roadmap(data: dict):
    if not data.get("steps"): raise ValueError("Empty roadmap")
    for s in data["steps"]:
        if "level" not in s: s["level"] = "Beginner"


def _get_key_from_config():
    try:
        from config import Config
        return getattr(Config, "GEMINI_API_KEY", None)
    except: return None
