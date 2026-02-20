"""
Rich, fully-detailed roadmap dataset for Learn with AK.
18 roadmaps across: IT, AI/ML, Cloud, Cyber, Govt, Finance,
Banking, Medical, Law, Marketing, Management, Core Engineering.
Every roadmap is complete: Beginner → Intermediate → Advanced.
"""

ALL_ROADMAPS = [

    # ══════════════════════════════════════════════
    # 1. FULL STACK DEVELOPER (MERN)
    # ══════════════════════════════════════════════
    {
        "title": "Full Stack Web Developer (MERN)",
        "description": "Master end-to-end web development using MongoDB, Express.js, React, and Node.js. Build and deploy production-ready applications.",
        "category": "Tech",
        "difficulty": "intermediate",
        "meta_data": {
            "skills": {"core": ["HTML/CSS", "JavaScript"], "technical": ["React", "Node.js", "MongoDB", "REST APIs"], "soft": ["Problem Solving", "Teamwork"]},
            "tools": ["VS Code", "Postman", "Docker", "GitHub"],
            "career_readiness": {"resume": ["Full Stack Projects", "GitHub Profile"], "interview": ["Live Coding", "System Design Basics"], "portfolio": "Deployed SaaS App"},
            "estimated_time": "8-10 Months",
            "career_progression": ["Junior Dev", "Full Stack Dev", "Tech Lead"]
        },
        "steps": [
            {"level": "Beginner", "title": "Web Foundations (HTML & CSS)", "desc": "Learn HTML5 semantics, CSS3 styling, Flexbox, Grid layout, and responsive design principles.", "resources": "MDN Web Docs | freeCodeCamp"},
            {"level": "Beginner", "title": "JavaScript Core", "desc": "Master ES6+ syntax, DOM manipulation, event handling, Fetch API, and asynchronous JavaScript (Promises, async/await).", "resources": "javascript.info | The Odin Project"},
            {"level": "Beginner", "title": "Version Control with Git & GitHub", "desc": "Learn branching, merging, pull requests, and collaborative workflows.", "resources": "Pro Git (free book) | GitHub Docs"},
            {"level": "Intermediate", "title": "React.js Frontend", "desc": "Build dynamic UIs with React — JSX, functional components, hooks (useState, useEffect), React Router, and Redux Toolkit.", "resources": "react.dev | Full Stack Open"},
            {"level": "Intermediate", "title": "Node.js & Express Backend", "desc": "Create RESTful APIs, handle middleware, authentication with JWT, and build MVC architecture.", "resources": "expressjs.com | Node.js Docs"},
            {"level": "Intermediate", "title": "MongoDB Database", "desc": "NoSQL design, CRUD operations with Mongoose, schema validation, indexing, and aggregation pipelines.", "resources": "MongoDB University (free)"},
            {"level": "Advanced", "title": "Authentication & Security", "desc": "Implement OAuth2, JWT refresh tokens, bcrypt hashing, CORS, rate limiting, and HTTPS.", "resources": "OWASP Top 10 | Auth0 Docs"},
            {"level": "Advanced", "title": "Testing & CI/CD", "desc": "Unit testing with Jest, integration testing, GitHub Actions pipelines, and automated deployment.", "resources": "Jest Docs | GitHub Actions Docs"},
            {"level": "Advanced", "title": "Deployment & DevOps", "desc": "Dockerize apps, deploy to AWS/Render/Vercel, configure domain, SSL, and environment variables.", "resources": "Docker Docs | AWS Free Tier"}
        ]
    },

    # ══════════════════════════════════════════════
    # 2. SOFTWARE ENGINEER (DSA + System Design)
    # ══════════════════════════════════════════════
    {
        "title": "Software Engineer (DSA + System Design)",
        "description": "Crack top tech company interviews with strong Data Structures, Algorithms, and System Design skills. From basics to FAANG-level preparation.",
        "category": "Tech",
        "difficulty": "advanced",
        "meta_data": {
            "skills": {"core": ["DSA", "OOP"], "technical": ["Java/C++/Python", "SQL", "System Design"], "soft": ["Communication", "Analytical Thinking"]},
            "tools": ["LeetCode", "IntelliJ/VS Code", "GitHub", "Jira"],
            "career_readiness": {"resume": ["LeetCode 200+ Problems", "Open Source Contributions"], "interview": ["System Design", "Behavioral (STAR)"], "portfolio": "Complex project on GitHub"},
            "estimated_time": "12-18 Months",
            "career_progression": ["SDE-I", "SDE-II", "Senior SDE", "Principal Engineer"]
        },
        "steps": [
            {"level": "Beginner", "title": "Choose a Programming Language", "desc": "Master one language deeply: Java, Python, or C++. Focus on syntax, OOP, collections, and I/O.", "resources": "GeeksForGeeks | CS50 (Harvard)"},
            {"level": "Beginner", "title": "Arrays, Strings & Recursion", "desc": "Foundation problems — sliding window, two pointers, prefix sums, and basic recursion patterns.", "resources": "LeetCode Easy | NeetCode.io"},
            {"level": "Beginner", "title": "Linked Lists, Stacks & Queues", "desc": "Understand pointer manipulation, reversal, cycle detection, and monotonic stacks.", "resources": "LeetCode Blind 75"},
            {"level": "Intermediate", "title": "Trees, Graphs & BFS/DFS", "desc": "Binary trees, BST operations, graph traversal, topological sort, and shortest paths (Dijkstra).", "resources": "William Fiset Graph Theory (YouTube)"},
            {"level": "Intermediate", "title": "Dynamic Programming", "desc": "Memoization, tabulation, 1D/2D DP, Knapsack, LCS, and common DP interview patterns.", "resources": "Aditya Verma DP Series (YouTube)"},
            {"level": "Intermediate", "title": "SQL & Database Basics", "desc": "Joins, subqueries, window functions, indexing, and ACID properties.", "resources": "SQLZoo | Mode SQL Tutorial"},
            {"level": "Advanced", "title": "Low-Level Design (LLD)", "desc": "SOLID principles, design patterns (Singleton, Factory, Observer, Strategy), and OOP case studies.", "resources": "Refactoring.guru | Grokking LLD"},
            {"level": "Advanced", "title": "High-Level Design (HLD)", "desc": "Scalability, load balancing, caching (Redis), message queues (Kafka), microservices, and CAP theorem.", "resources": "System Design Primer (GitHub)"},
            {"level": "Advanced", "title": "Mock Interviews & Competitive Practice", "desc": "Timed contests, mock system design rounds, STAR behavioral prep.", "resources": "Pramp | Interviewing.io | Codeforces"}
        ]
    },

    # ══════════════════════════════════════════════
    # 3. ARTIFICIAL INTELLIGENCE ENGINEER
    # ══════════════════════════════════════════════
    {
        "title": "Artificial Intelligence Engineer",
        "description": "Build AI systems from scratch — from classical ML to deep learning, NLP, and deploying AI products into production.",
        "category": "Data & AI",
        "difficulty": "advanced",
        "meta_data": {
            "skills": {"core": ["Math (Linear Algebra, Calculus)", "Python", "Statistics"], "technical": ["TensorFlow", "PyTorch", "Scikit-learn", "LLMs"], "soft": ["Research Mindset", "Creativity"]},
            "tools": ["Jupyter Notebook", "Google Colab", "Hugging Face", "MLflow", "Docker"],
            "career_readiness": {"resume": ["Kaggle Medals", "Research Papers", "AI Projects"], "interview": ["ML Theory + Coding", "Case Studies"], "portfolio": "AI Demo Apps (HuggingFace Spaces)"},
            "estimated_time": "12-18 Months",
            "career_progression": ["ML Engineer", "Senior AI Engineer", "AI Research Scientist"]
        },
        "steps": [
            {"level": "Beginner", "title": "Python for AI (NumPy, Pandas)", "desc": "Arrays, DataFrames, vectorized operations, data cleaning, and EDA.", "resources": "Kaggle Learn (free) | CS231n"},
            {"level": "Beginner", "title": "Math for ML", "desc": "Linear algebra (matrices, eigenvectors), calculus (gradients, chain rule), probability, and statistics.", "resources": "3Blue1Brown (YouTube) | Khan Academy"},
            {"level": "Beginner", "title": "Classical Machine Learning", "desc": "Supervised (regression, classification), unsupervised (clustering), model evaluation, and cross-validation.", "resources": "Scikit-learn Docs | Google ML Crash Course"},
            {"level": "Intermediate", "title": "Data Visualization & EDA", "desc": "Matplotlib, Seaborn, Plotly, and storytelling with data.", "resources": "DataCamp | Kaggle Notebooks"},
            {"level": "Intermediate", "title": "Deep Learning Fundamentals", "desc": "Neural networks, backpropagation, CNNs, RNNs, and transfer learning.", "resources": "fast.ai (free) | DeepLearning.AI"},
            {"level": "Intermediate", "title": "Natural Language Processing (NLP)", "desc": "Tokenization, embeddings, BERT, fine-tuning LLMs, and RAG architectures.", "resources": "Hugging Face Course (free)"},
            {"level": "Advanced", "title": "Generative AI & LLMs", "desc": "Prompt engineering, fine-tuning GPT/Llama, LangChain pipelines, and vector databases.", "resources": "LangChain Docs | Andrej Karpathy YouTube"},
            {"level": "Advanced", "title": "MLOps & Model Deployment", "desc": "ML pipelines (MLflow), model serving (FastAPI), containerization (Docker), and cloud deployment.", "resources": "MLflow Docs | Made with ML"},
            {"level": "Advanced", "title": "AI Research & Specialization", "desc": "Read papers (ArXiv), implement SOTA models, specialize in Computer Vision, NLP, or RL.", "resources": "Papers With Code | Two Minute Papers (YouTube)"}
        ]
    },

    # ══════════════════════════════════════════════
    # 4. DATA SCIENTIST
    # ══════════════════════════════════════════════
    {
        "title": "Data Scientist",
        "description": "Extract actionable insights from data using statistics, machine learning, and compelling visualizations. Build models that drive real business decisions.",
        "category": "Data & AI",
        "difficulty": "advanced",
        "meta_data": {
            "skills": {"core": ["Statistics", "Python/R"], "technical": ["Pandas", "Scikit-learn", "SQL", "Tableau"], "soft": ["Curiosity", "Communication"]},
            "tools": ["Jupyter", "Tableau", "BigQuery", "Snowflake"],
            "career_readiness": {"resume": ["Kaggle Competitions", "Published Analysis"], "interview": ["Stats & Probability", "Case Studies"], "portfolio": "Data Blog / GitHub"},
            "estimated_time": "10-14 Months",
            "career_progression": ["Junior Data Scientist", "Senior Data Scientist", "Lead Data Scientist", "Chief Data Officer"]
        },
        "steps": [
            {"level": "Beginner", "title": "Python for Data Analysis", "desc": "NumPy arrays, Pandas DataFrames, data cleaning, and handling missing values.", "resources": "Kaggle Python & Pandas courses (free)"},
            {"level": "Beginner", "title": "Statistics & Probability", "desc": "Descriptive stats, probability distributions, hypothesis testing, p-values, and confidence intervals.", "resources": "Khan Academy Stats | StatQuest (YouTube)"},
            {"level": "Beginner", "title": "SQL for Data Science", "desc": "SELECT, JOIN, GROUP BY, window functions, and writing complex analytical queries.", "resources": "Mode SQL Tutorial | LeetCode SQL"},
            {"level": "Intermediate", "title": "Data Visualization", "desc": "Matplotlib, Seaborn, Plotly, and building Tableau dashboards for stakeholder communication.", "resources": "DataCamp | Tableau Public"},
            {"level": "Intermediate", "title": "Machine Learning for Data Science", "desc": "Regression, classification, clustering, feature engineering, and hyperparameter tuning.", "resources": "Hands-On ML (book) | fast.ai"},
            {"level": "Intermediate", "title": "A/B Testing & Experimentation", "desc": "Design experiments, statistical significance, p-value interpretation, and business decision making.", "resources": "Udacity A/B Testing Course"},
            {"level": "Advanced", "title": "Big Data Tools", "desc": "Spark, Hadoop basics, working with large datasets on cloud platforms (GCP BigQuery, AWS Redshift).", "resources": "Databricks Academy | Google BigQuery Docs"},
            {"level": "Advanced", "title": "Advanced ML & Feature Engineering", "desc": "Ensemble methods, XGBoost, LGBM, SHAP values, and automated feature selection.", "resources": "Kaggle Competition Solutions"},
            {"level": "Advanced", "title": "Data Science in Production", "desc": "ML in production, model monitoring, drift detection, and reporting to stakeholders.", "resources": "Full Stack Deep Learning | Evidently AI Docs"}
        ]
    },

    # ══════════════════════════════════════════════
    # 5. CLOUD ENGINEER (AWS)
    # ══════════════════════════════════════════════
    {
        "title": "AWS Cloud Engineer",
        "description": "Design, deploy, and manage cloud infrastructure on Amazon Web Services. Work towards the Solutions Architect certification.",
        "category": "Cloud & DevOps",
        "difficulty": "advanced",
        "meta_data": {
            "skills": {"core": ["Networking", "Linux CLI"], "technical": ["EC2", "S3", "VPC", "Lambda", "RDS", "IAM"], "soft": ["Troubleshooting", "Documentation"]},
            "tools": ["AWS Console", "AWS CLI", "Terraform", "CloudFormation"],
            "career_readiness": {"resume": ["AWS Certified Solutions Architect – Associate"], "interview": ["Architecture Scenarios", "Cost Optimization"], "portfolio": "Terraform Cloud Templates"},
            "estimated_time": "6-9 Months",
            "career_progression": ["Cloud Admin", "Cloud Engineer", "Solutions Architect", "Cloud Architect"]
        },
        "steps": [
            {"level": "Beginner", "title": "Cloud Computing Fundamentals", "desc": "IaaS vs PaaS vs SaaS, public vs private cloud, regions, availability zones, and cloud economics.", "resources": "AWS Cloud Practitioner Essentials (free)"},
            {"level": "Beginner", "title": "AWS Core Services", "desc": "EC2 instances, S3 storage, IAM roles/policies, RDS databases, and basic networking.", "resources": "AWS Documentation | A Cloud Guru"},
            {"level": "Beginner", "title": "Linux & Bash for Cloud", "desc": "File system navigation, cron jobs, shell scripting, SSH, and package management.", "resources": "Linux Journey | OverTheWire"},
            {"level": "Intermediate", "title": "VPC & Networking on AWS", "desc": "Custom VPCs, subnets, route tables, NAT gateways, security groups, NACLs, and VPN connections.", "resources": "Adrian Cantrill AWS Courses"},
            {"level": "Intermediate", "title": "Serverless & Managed Services", "desc": "AWS Lambda, API Gateway, DynamoDB, SQS, SNS, CloudWatch monitoring, and event-driven architecture.", "resources": "Serverless Land | AWS Docs"},
            {"level": "Intermediate", "title": "Infrastructure as Code (Terraform)", "desc": "Write, plan, and apply Terraform configurations to manage AWS resources declaratively.", "resources": "Terraform Docs | HashiCorp Learn"},
            {"level": "Advanced", "title": "High Availability & Disaster Recovery", "desc": "Multi-AZ, auto-scaling groups, load balancers (ALB/NLB), RTO/RPO planning, and backup strategies.", "resources": "AWS Well-Architected Framework"},
            {"level": "Advanced", "title": "Security & Compliance", "desc": "AWS GuardDuty, CloudTrail, KMS encryption, Config Rules, and shared responsibility model.", "resources": "AWS Security Specialty Prep"},
            {"level": "Advanced", "title": "Solutions Architect Certification Prep", "desc": "Practice exams, architectural case studies, cost optimization, and AWS certification exam.", "resources": "TutorialsDojo | AWS Practice Exams"}
        ]
    },

    # ══════════════════════════════════════════════
    # 6. DEVOPS ENGINEER
    # ══════════════════════════════════════════════
    {
        "title": "DevOps Engineer",
        "description": "Bridge development and operations — automate pipelines, manage containers, and keep production systems reliable, fast, and secure.",
        "category": "Cloud & DevOps",
        "difficulty": "advanced",
        "meta_data": {
            "skills": {"core": ["Linux", "Bash Scripting", "Networking"], "technical": ["Docker", "Kubernetes", "CI/CD", "Terraform", "Prometheus"], "soft": ["Collaboration", "Incident Response"]},
            "tools": ["Docker", "Kubernetes", "Jenkins", "GitHub Actions", "Grafana", "Ansible"],
            "career_readiness": {"resume": ["CKA Certification", "Open Source Contributions"], "interview": ["SRE Scenarios", "Debugging Under Pressure"], "portfolio": "Live K8s Dashboard"},
            "estimated_time": "10-14 Months",
            "career_progression": ["Junior DevOps", "DevOps Engineer", "SRE", "Platform Engineer"]
        },
        "steps": [
            {"level": "Beginner", "title": "Linux Administration", "desc": "Filesystem, user management, process control, logs, cron, SSH, and shell scripting.", "resources": "The Linux Command Line (free book)"},
            {"level": "Beginner", "title": "Git & Version Control Workflows", "desc": "Git branching strategies (Gitflow, trunk-based), code review, and monorepo vs multirepo.", "resources": "Atlassian Git Tutorials"},
            {"level": "Beginner", "title": "Networking Essentials", "desc": "DNS, HTTP/HTTPS, TCP/UDP, load balancers, firewalls, and reverse proxies (Nginx).", "resources": "Julia Evans Networking Zines"},
            {"level": "Intermediate", "title": "Docker & Containerization", "desc": "Dockerfiles, images, containers, volumes, networking, and Docker Compose for multi-service apps.", "resources": "Docker Docs | Docker in 100 Seconds (YouTube)"},
            {"level": "Intermediate", "title": "CI/CD Pipelines", "desc": "Build, test, and deploy automation with GitHub Actions, Jenkins, or GitLab CI. Blue/green and canary deployments.", "resources": "GitHub Actions Docs | CloudBees Blog"},
            {"level": "Intermediate", "title": "Kubernetes (K8s)", "desc": "Pods, deployments, services, ingress, ConfigMaps, secrets, RBAC, and Helm charts.", "resources": "Kubernetes Docs | KodeKloud (free tier)"},
            {"level": "Advanced", "title": "Infrastructure as Code", "desc": "Terraform for cloud provisioning, Ansible for configuration management, idempotency, and state management.", "resources": "HashiCorp Learn | Ansible Docs"},
            {"level": "Advanced", "title": "Monitoring & Observability", "desc": "Prometheus metrics, Grafana dashboards, ELK stack for logging, and alerting strategies.", "resources": "Grafana Learn | Elastic Docs"},
            {"level": "Advanced", "title": "Site Reliability Engineering (SRE)", "desc": "SLAs/SLOs/SLIs, incident management, chaos engineering, and on-call best practices.", "resources": "Google SRE Book (free online)"}
        ]
    },

    # ══════════════════════════════════════════════
    # 7. CYBERSECURITY / ETHICAL HACKER
    # ══════════════════════════════════════════════
    {
        "title": "Cybersecurity & Ethical Hacking",
        "description": "Learn to identify, exploit, and defend against cyber threats. Progress from networking basics to running full penetration tests and earning bug bounties.",
        "category": "Cyber Security",
        "difficulty": "advanced",
        "meta_data": {
            "skills": {"core": ["Networking", "Linux", "Python"], "technical": ["Penetration Testing", "Web App Security", "Network Security", "OSINT"], "soft": ["Ethics", "Attention to Detail"]},
            "tools": ["Kali Linux", "Metasploit", "Burp Suite", "Nmap", "Wireshark"],
            "career_readiness": {"resume": ["CEH / OSCP Certification", "Bug Bounty Findings"], "interview": ["Vulnerability Assessment Scenarios"], "portfolio": "HackTheBox / Bug Bounty Profile"},
            "estimated_time": "12-15 Months",
            "career_progression": ["SOC Analyst", "Penetration Tester", "Security Engineer", "CISO"]
        },
        "steps": [
            {"level": "Beginner", "title": "Networking Fundamentals", "desc": "OSI model, TCP/IP, DNS, HTTP/S, ports and protocols, subnetting, and packet analysis with Wireshark.", "resources": "CompTIA Network+ Study Guide | Professor Messer"},
            {"level": "Beginner", "title": "Linux for Security", "desc": "CLI navigation, permissions, bash scripting, process management, and Kali Linux setup.", "resources": "Linux Journey | OverTheWire: Bandit"},
            {"level": "Beginner", "title": "Python for Hackers", "desc": "Writing scanners, automating tasks, socket programming, and simple exploit scripts.", "resources": "Automate the Boring Stuff (free)"},
            {"level": "Intermediate", "title": "Reconnaissance & OSINT", "desc": "Footprinting, Nmap scanning, Shodan, TheHarvester, Google dorking, and social engineering basics.", "resources": "TryHackMe: Pre-Security | OSINT Framework"},
            {"level": "Intermediate", "title": "Web Application Security", "desc": "OWASP Top 10 — SQL Injection, XSS, CSRF, IDOR, SSRF. Using Burp Suite for interception.", "resources": "PortSwigger Web Security Academy (free)"},
            {"level": "Intermediate", "title": "Network Penetration Testing", "desc": "Vulnerability scanning (Nessus), ARP spoofing, MitM attacks, and wireless attacks (WPA2).", "resources": "TCM Security Courses | HackTheBox"},
            {"level": "Advanced", "title": "Exploitation & Post-Exploitation", "desc": "Metasploit Framework, custom payloads, privilege escalation (Linux/Windows), and persistence.", "resources": "HackTheBox | PEN-200 (OSCP prep)"},
            {"level": "Advanced", "title": "Active Directory & Windows Attacks", "desc": "Kerberoasting, Pass-the-Hash, BloodHound, credential dumping, and PowerShell attacks.", "resources": "HTB Academy: Active Directory"},
            {"level": "Advanced", "title": "Bug Bounty & Certifications", "desc": "Participate in HackerOne/Bugcrowd programs, build a report portfolio, and pursue CEH/OSCP.", "resources": "HackerOne Hacktivity | Bugcrowd University"}
        ]
    },

    # ══════════════════════════════════════════════
    # 8. ANDROID / MOBILE APP DEVELOPER
    # ══════════════════════════════════════════════
    {
        "title": "Android App Developer (Kotlin)",
        "description": "Build native Android applications from scratch using Kotlin, Jetpack Compose, and Firebase. Publish your apps on the Google Play Store.",
        "category": "Tech",
        "difficulty": "intermediate",
        "meta_data": {
            "skills": {"core": ["Kotlin/Java", "OOP"], "technical": ["Jetpack Compose", "Room", "Retrofit", "Firebase"], "soft": ["UX Thinking", "Attention to Detail"]},
            "tools": ["Android Studio", "Firebase Console", "Figma", "Google Play Console"],
            "career_readiness": {"resume": ["Play Store Published Apps", "GitHub Repos"], "interview": ["Android Architecture", "Performance Optimization"], "portfolio": "2-3 Published Apps"},
            "estimated_time": "8-12 Months",
            "career_progression": ["Junior Android Dev", "Android Developer", "Senior Mobile Engineer", "Mobile Architect"]
        },
        "steps": [
            {"level": "Beginner", "title": "Kotlin Fundamentals", "desc": "Syntax, null safety, data classes, lambdas, coroutines basics, and Kotlin idioms.", "resources": "Kotlin Docs | Google Kotlin Bootcamp (free)"},
            {"level": "Beginner", "title": "Android Basics & Android Studio", "desc": "Activities, fragments, layouts (XML), Android lifecycle, intents, and permissions.", "resources": "Google Android Basics (free)"},
            {"level": "Beginner", "title": "UI with Jetpack Compose", "desc": "Declarative UI, Composable functions, state management, theming, and Material 3.", "resources": "Compose Docs | Android Codelab"},
            {"level": "Intermediate", "title": "Navigation & Architecture", "desc": "Navigation component, MVVM pattern, ViewModel, LiveData/StateFlow, and Clean Architecture.", "resources": "Android Architecture Guide (Google)"},
            {"level": "Intermediate", "title": "Local Data & Networking", "desc": "Room database (SQLite), Retrofit for REST APIs, Moshi/Gson parsing, and coroutine-based networking.", "resources": "Android Developer Guides"},
            {"level": "Intermediate", "title": "Firebase Integration", "desc": "Firebase Auth, Firestore real-time DB, Cloud Storage, FCM push notifications, and Analytics.", "resources": "Firebase Docs (Google)"},
            {"level": "Advanced", "title": "Performance & Testing", "desc": "Profiling, lazy loading, memory leaks (LeakCanary), unit tests (JUnit), and UI tests (Espresso).", "resources": "Android Performance Docs"},
            {"level": "Advanced", "title": "Publishing to Google Play", "desc": "Signing APK/AAB, Play Console setup, beta testing tracks, store listing optimization (ASO).", "resources": "Google Play Academy"},
            {"level": "Advanced", "title": "Advanced Topics", "desc": "WorkManager, background tasks, custom animations, dependency injection (Hilt/Dagger), and modularization.", "resources": "Android Dev Summit Talks | YouTube"}
        ]
    },

    # ══════════════════════════════════════════════
    # 9. UI/UX DESIGNER
    # ══════════════════════════════════════════════
    {
        "title": "UI/UX Designer",
        "description": "Design beautiful, user-centered digital products. Learn research, wireframing, prototyping, and design systems used at top product companies.",
        "category": "Tech",
        "difficulty": "beginner",
        "meta_data": {
            "skills": {"core": ["User Research", "Visual Design"], "technical": ["Figma", "Prototyping", "Design Systems", "Accessibility"], "soft": ["Empathy", "Communication"]},
            "tools": ["Figma", "Adobe XD", "Maze", "Miro", "Notion"],
            "career_readiness": {"resume": ["Portfolio with 3-5 Case Studies"], "interview": ["Design Critique", "Design Challenge (48h)"], "portfolio": "Behance / Personal Site"},
            "estimated_time": "6-10 Months",
            "career_progression": ["Junior UX Designer", "Product Designer", "Senior Designer", "Head of Design"]
        },
        "steps": [
            {"level": "Beginner", "title": "Design Principles & Theory", "desc": "Gestalt principles, visual hierarchy, typography, color theory, spacing, and grid systems.", "resources": "Refactoring UI (book) | Google Material Design"},
            {"level": "Beginner", "title": "User Research Methods", "desc": "User interviews, surveys, competitive analysis, empathy maps, and defining user personas.", "resources": "Nielsen Norman Group Articles (free)"},
            {"level": "Beginner", "title": "Wireframing & Information Architecture", "desc": "Lo-fi wireframes, user flows, site maps, card sorting, and how to use Miro/FigJam.", "resources": "Figma Community Templates"},
            {"level": "Intermediate", "title": "Figma for UI Design", "desc": "Components, auto-layout, variants, styles, and building pixel-perfect hi-fi mockups.", "resources": "Figma Academy | DesignCourse YouTube"},
            {"level": "Intermediate", "title": "Prototyping & Usability Testing", "desc": "Interactive Figma prototypes, conduct usability tests, analyze recordings, and iterate.", "resources": "Maze | Lookback.io"},
            {"level": "Intermediate", "title": "Design Systems", "desc": "Build reusable component libraries, token-based design, documentation, and handoff to developers.", "resources": "Storybook Docs | Material Design 3"},
            {"level": "Advanced", "title": "Accessibility (a11y)", "desc": "WCAG 2.1 standards, color contrast, keyboard navigation, screen reader support, and inclusive design.", "resources": "a11y Project | WebAIM"},
            {"level": "Advanced", "title": "Product Thinking & Metrics", "desc": "North Star metric, conversion funnels, A/B testing designs, and collaborating with PMs.", "resources": "Lenny's Newsletter | ProductHunt"},
            {"level": "Advanced", "title": "Portfolio & Career Prep", "desc": "Write compelling UX case studies, prepare for design critiques, and craft a standout portfolio site.", "resources": "UX Folio | Career Foundry Guide"}
        ]
    },

    # ══════════════════════════════════════════════
    # 10. CIVIL SERVICES OFFICER (IAS/IPS)
    # ══════════════════════════════════════════════
    {
        "title": "Civil Services Officer (IAS/IPS – UPSC)",
        "description": "Comprehensive preparation roadmap for the UPSC Civil Services Examination — Prelims, Mains, and Personality Test (Interview).",
        "category": "Government",
        "difficulty": "advanced",
        "meta_data": {
            "skills": {"core": ["General Studies", "Essay Writing", "Current Affairs"], "technical": ["Public Administration", "International Relations", "Economy"], "soft": ["Leadership", "Decision Making", "Integrity"]},
            "tools": ["The Hindu / Indian Express", "NCERTs", "Vision IAS / Insights IAS", "PYQs"],
            "career_readiness": {"resume": ["N/A – Exam Based"], "interview": ["UPSC Personality Test (Panel Interview)"], "portfolio": "N/A"},
            "estimated_time": "18-24 Months",
            "career_progression": ["SDM / ASP", "District Magistrate / SP", "Secretary / DGP", "Cabinet Secretary / DGP State"]
        },
        "steps": [
            {"level": "Beginner", "title": "NCERT Foundation (Class 6–12)", "desc": "Read all NCERTs for History, Geography, Polity, Economy, Science. Build your conceptual base.", "resources": "NCERT Textbooks (free PDF on ncert.nic.in)"},
            {"level": "Beginner", "title": "Standard Reference Books", "desc": "Laxmikanth (Indian Polity), Spectrum (Modern History), Ramesh Singh (Economy), G C Leong (Geography).", "resources": "PMF IAS | Study IQ Resources"},
            {"level": "Beginner", "title": "Daily Newspaper Reading Habit", "desc": "The Hindu editorial analysis, PIB summaries, and monthly current affairs magazines.", "resources": "Vision IAS Monthly Magazine | Insights Daily CA"},
            {"level": "Intermediate", "title": "UPSC Prelims Strategy", "desc": "GS Paper 1 syllabus coverage, CSAT practice (Paper 2), solving 10+ years' PYQs.", "resources": "Drishti IAS PYQs | Insights Prelims Test Series"},
            {"level": "Intermediate", "title": "UPSC Mains GS Paper Writing", "desc": "Daily mains answer writing (150/250 words), structuring answers, diagrams, and flowcharts.", "resources": "ForumIAS Answer Writing | Insights Secure Initiative"},
            {"level": "Intermediate", "title": "Optional Subject Preparation", "desc": "Choose optional (PSIR, History, Sociology, Geography preferred), study standard texts thoroughly.", "resources": "IASbaba | Optional Toppers' Notes"},
            {"level": "Advanced", "title": "Essay Writing Mastery", "desc": "Practice 2+ essays/week, philosophical and policy topics, structure, depth, real examples, and language.", "resources": "Insights Essay Archive"},
            {"level": "Advanced", "title": "Ethics, Integrity & Aptitude (GS IV)", "desc": "Thinkers, case studies, values in public service, emotional intelligence, and moral dilemmas.", "resources": "Lexicon for Ethics | G Subba Rao"},
            {"level": "Advanced", "title": "Personality Test (Interview) Prep", "desc": "DAF filling, current affairs mock interviews, confidence building, and self-awareness.", "resources": "ForumIAS Mock Interviews | Insights PT Programme"}
        ]
    },

    # ══════════════════════════════════════════════
    # 11. BANK PO / GOVERNMENT BANKING
    # ══════════════════════════════════════════════
    {
        "title": "Bank Probationary Officer (Bank PO)",
        "description": "Crack competitive exams like IBPS PO, SBI PO, and RBI Grade B to begin a prestigious government banking career.",
        "category": "Government",
        "difficulty": "intermediate",
        "meta_data": {
            "skills": {"core": ["Quantitative Aptitude", "Reasoning", "English"], "technical": ["Banking Awareness", "Computer Knowledge", "Current Affairs"], "soft": ["Time Management", "Accuracy"]},
            "tools": ["Banking Exam Prep Apps", "Mock Test Platforms", "Oliveboard / Adda247", "Newspapers"],
            "career_readiness": {"resume": ["N/A – Exam Based"], "interview": ["Banking/HR Interview"], "portfolio": "N/A"},
            "estimated_time": "6-12 Months",
            "career_progression": ["Probationary Officer", "Assistant Manager", "Branch Manager", "General Manager"]
        },
        "steps": [
            {"level": "Beginner", "title": "Understand Exam Pattern & Syllabus", "desc": "Study IBPS PO / SBI PO notification carefully. Understand sectional cut-offs, marking scheme, and stages.", "resources": "IBPS.in | SBI.co.in Official Websites"},
            {"level": "Beginner", "title": "Quantitative Aptitude Basics", "desc": "Number system, percentages, ratios, averages, simple/compound interest, and profit-loss.", "resources": "R.S. Aggarwal Quant | Adda247 YouTube"},
            {"level": "Beginner", "title": "Reasoning Ability Foundation", "desc": "Puzzles, seating arrangements, syllogisms, blood relations, directions, and coding-decoding.", "resources": "Reasoning by MK Pandey | Oliveboard"},
            {"level": "Intermediate", "title": "English Language Skills", "desc": "Reading comprehension, error spotting, fill in the blanks, cloze test, parajumbles.", "resources": "The Hindu Editorial Practice | MB Publication"},
            {"level": "Intermediate", "title": "Banking & Financial Awareness", "desc": "RBI functions, monetary policy, types of banks, important financial terms, budget, and schemes.", "resources": "GKToday | Banking Awareness by Arihant"},
            {"level": "Intermediate", "title": "Current Affairs & General Knowledge", "desc": "Daily news, government schemes, important awards, sports, international events (last 6 months).", "resources": "Monthly Affairs by Adda247 | Capsule PDFs"},
            {"level": "Advanced", "title": "Mock Tests & Time Management", "desc": "Take full-length mocks 3x/week, analyze weak areas, speed improvement, and accuracy drills.", "resources": "Oliveboard | Testbook | Gradeup (BYJU's Exam Prep)"},
            {"level": "Advanced", "title": "Descriptive Writing (Letter/Essay)", "desc": "SBI PO mains has descriptive paper — practice formal letters, essay writing on finance/social topics.", "resources": "SBI PO Previous Papers"},
            {"level": "Advanced", "title": "Group Discussion & Banking Interview Prep", "desc": "Practice GD topics (economy, digitization, banking), work on communication, and prepare bank-specific questions.", "resources": "Interview Mocha | Bank Interview Books"}
        ]
    },

    # ══════════════════════════════════════════════
    # 12. CHARTERED ACCOUNTANT (CA)
    # ══════════════════════════════════════════════
    {
        "title": "Chartered Accountant (CA)",
        "description": "India's most respected finance credential. Master accounting, auditing, taxation, and financial management through the ICAI's structured CA program.",
        "category": "Finance",
        "difficulty": "advanced",
        "meta_data": {
            "skills": {"core": ["Accounting", "Law", "Taxation"], "technical": ["Financial Reporting (IFRS/Ind AS)", "Audit", "Direct & Indirect Tax"], "soft": ["Integrity", "Analytical Thinking"]},
            "tools": ["Tally ERP", "Excel", "ICAI Study Material", "GST Portal", "Income Tax Portal"],
            "career_readiness": {"resume": ["CA Certificate", "Articleship Experience"], "interview": ["Technical Finance", "Practical Taxation"], "portfolio": "Articleship Portfolio"},
            "estimated_time": "4.5-5 Years",
            "career_progression": ["CA Fresher", "Senior CA", "Manager-Finance", "CFO"]
        },
        "steps": [
            {"level": "Beginner", "title": "Foundation Course (4 Subjects)", "desc": "Principles of Accounting, Business Laws, Business Mathematics & Statistics, Business Economics.", "resources": "ICAI Study Material | CA Foundation Books"},
            {"level": "Beginner", "title": "Intermediate Group I", "desc": "Advanced Accounting (AS-based), Corporate & Other Laws, Taxation (IT + GST basics).", "resources": "ICAI ICITSS | ICAI E-Portal"},
            {"level": "Intermediate", "title": "Intermediate Group II", "desc": "Cost & Management Accounting, Auditing & Assurance, Enterprise IT & Strategic Management.", "resources": "ICAI SM | ICAI Mock Tests"},
            {"level": "Intermediate", "title": "Articleship Training (3 Years)", "desc": "Practical exposure in audit firms or companies — GST filing, income tax returns, financial statements, and audits.", "resources": "CA Firm Experience | ICAI UDIN Portal"},
            {"level": "Intermediate", "title": "ICITSS & AICITSS Training", "desc": "Mandatory IT training and Advanced IT training modules by ICAI.", "resources": "ICAI ICITSS Portal"},
            {"level": "Advanced", "title": "CA Final Group I", "desc": "Financial Reporting (Ind AS/IFRS), Strategic Financial Management, Advanced Auditing.", "resources": "ICAI SM | CA Study Groups"},
            {"level": "Advanced", "title": "CA Final Group II", "desc": "Direct Tax Laws & International Tax, Indirect Tax Laws (GST), Strategic Cost Management, Risk.", "resources": "ICAI E-Lectures | Revision Test Series"},
            {"level": "Advanced", "title": "Exam Strategy & Mock Tests", "desc": "Attempt MTs, revision of suggested answers, time management per paper, and presentation skills.", "resources": "ICAI Mock Test Series | Past Exam Analysis"},
            {"level": "Advanced", "title": "Membership & CPE", "desc": "Apply for ICAI membership, commence CPE hours, and specialize (DISA, Forensic Accounting, IFRS).", "resources": "ICAI Membership Portal"}
        ]
    },

    # ══════════════════════════════════════════════
    # 13. INVESTMENT BANKER / FINANCE PROFESSIONAL
    # ══════════════════════════════════════════════
    {
        "title": "Investment Banker & Financial Analyst",
        "description": "Break into the high-finance world of investment banking, M&A, and equity research. Build financial models and advise on billion-dollar deals.",
        "category": "Finance",
        "difficulty": "advanced",
        "meta_data": {
            "skills": {"core": ["Accounting", "Corporate Finance"], "technical": ["Financial Modeling", "Excel/VBA", "Valuation (DCF, Comps, LBO)"], "soft": ["Attention to Detail", "High-Pressure Tolerance"]},
            "tools": ["Excel", "Bloomberg Terminal", "PowerPoint", "FactSet", "Capital IQ"],
            "career_readiness": {"resume": ["CFA Level 1", "Internship at Bank/PE"], "interview": ["Technical Finance", "Behavioral (Fit)"], "portfolio": "Stock Pitch Deck"},
            "estimated_time": "12-24 Months",
            "career_progression": ["Analyst", "Associate", "VP", "Director", "Managing Director"]
        },
        "steps": [
            {"level": "Beginner", "title": "Financial Accounting Mastery", "desc": "Three financial statements (IS, BS, CF), ratio analysis, linking statements, and adjustments.", "resources": "Investopedia | Corporate Finance Institute (CFI)"},
            {"level": "Beginner", "title": "Excel for Finance", "desc": "Shortcuts, VLOOKUP/INDEX-MATCH, pivot tables, data validation, VBA macros, and scenario modeling.", "resources": "CFI Excel Course (free) | ExcelJet"},
            {"level": "Beginner", "title": "Corporate Finance Fundamentals", "desc": "Time Value of Money, NPV, IRR, WACC, CAPM, capital structure, and dividend policy.", "resources": "Damodaran Online (free) | CFA Curriculum"},
            {"level": "Intermediate", "title": "Financial Modeling (3-Statement Model)", "desc": "Build integrated income statement, balance sheet, and cash flow model from scratch in Excel.", "resources": "Breaking Into Wall Street (BIWS) | CFI"},
            {"level": "Intermediate", "title": "Valuation Methods", "desc": "DCF (discounted cash flow), comparable company analysis (comps), precedent transactions, and EV/EBITDA.", "resources": "Damodaran Valuation (book) | BIWS"},
            {"level": "Intermediate", "title": "M&A & Deal Structuring", "desc": "Merger models, accretion/dilution analysis, synergies, deal process, and due diligence.", "resources": "Mergers & Inquisitions | WSO"},
            {"level": "Advanced", "title": "Leveraged Buyout (LBO) Modeling", "desc": "MOIC/IRR calculation, debt structure, sponsor returns, and private equity case study.", "resources": "BIWS LBO Module | 10-K Reports"},
            {"level": "Advanced", "title": "Industry Research & Sector Knowledge", "desc": "Sector-specific metrics, reading equity research reports, identifying investment themes.", "resources": "Bloomberg / Reuters (library access) | Seeking Alpha"},
            {"level": "Advanced", "title": "CFA Prep & Networking", "desc": "CFA Level 1 study plan, networking on LinkedIn, informational interviews, and reaching out to bankers.", "resources": "CFA Institute | Wall Street Prep"}
        ]
    },

    # ══════════════════════════════════════════════
    # 14. DIGITAL MARKETING SPECIALIST
    # ══════════════════════════════════════════════
    {
        "title": "Digital Marketing Specialist",
        "description": "Drive online growth through SEO, paid ads, social media, content marketing, and analytics. Master the tools top brands use every day.",
        "category": "Marketing",
        "difficulty": "beginner",
        "meta_data": {
            "skills": {"core": ["SEO", "Content Creation", "Analytics"], "technical": ["Google Ads", "Meta Ads", "Email Marketing", "GA4"], "soft": ["Creativity", "Data-Driven Thinking"]},
            "tools": ["Google Analytics 4", "Semrush", "Mailchimp", "Canva", "Meta Ads Manager", "HubSpot"],
            "career_readiness": {"resume": ["Google Ads Certificate", "GA4 Certificate", "Portfolio of Campaigns"], "interview": ["Case Studies", "Campaign P&L"], "portfolio": "Live Campaign Results / Blog"},
            "estimated_time": "5-8 Months",
            "career_progression": ["Marketing Executive", "Digital Marketing Manager", "Growth Lead", "CMO"]
        },
        "steps": [
            {"level": "Beginner", "title": "Digital Marketing Fundamentals", "desc": "Marketing funnel (AIDA), digital channels overview, buyer personas, and setting SMART goals.", "resources": "Google Digital Garage (free certificate)"},
            {"level": "Beginner", "title": "Search Engine Optimization (SEO)", "desc": "Keyword research (Semrush/Ahrefs), on-page SEO, technical SEO, link building, and Google Search Console.", "resources": "Moz Beginner's Guide to SEO (free) | Ahrefs Blog"},
            {"level": "Beginner", "title": "Content Marketing & Copywriting", "desc": "Blog writing, content calendars, headlines, CTAs, and repurposing content across channels.", "resources": "Hubspot Blog | Copyblogger"},
            {"level": "Intermediate", "title": "Social Media Marketing", "desc": "Platform algorithms (Instagram, LinkedIn, YouTube), organic growth, scheduling, and community management.", "resources": "Hootsuite Blog | Buffer Academy"},
            {"level": "Intermediate", "title": "Paid Advertising (Google & Meta Ads)", "desc": "Campaign structure, audience targeting, bid strategies, A/B testing creatives, and ROAS optimization.", "resources": "Google Skillshop (free) | Meta Blueprint (free)"},
            {"level": "Intermediate", "title": "Email Marketing & Marketing Automation", "desc": "List segmentation, drip campaigns, open/click rates, and automation with Mailchimp/HubSpot.", "resources": "Mailchimp Academy (free) | HubSpot Academy"},
            {"level": "Advanced", "title": "Google Analytics 4 (GA4) & Data", "desc": "Event tracking, conversion setup, funnels, cohort analysis, and linking GA4 with Google Ads.", "resources": "Google Analytics Academy (free)"},
            {"level": "Advanced", "title": "Growth Hacking & CRO", "desc": "Conversion rate optimization, landing page A/B tests, heatmaps (Hotjar), and funnel analysis.", "resources": "GrowthHackers | Unbounce Blog"},
            {"level": "Advanced", "title": "Personal Brand & Agency/In-House", "desc": "Build a personal brand, manage a client account end-to-end, and prepare a performance-based portfolio.", "resources": "Marketing School Podcast | Neil Patel Blog"}
        ]
    },

    # ══════════════════════════════════════════════
    # 15. PRODUCT MANAGER
    # ══════════════════════════════════════════════
    {
        "title": "Product Manager (Tech)",
        "description": "Lead products from idea to launch. Master user research, roadmapping, data analysis, and cross-functional collaboration to build products users love.",
        "category": "Management",
        "difficulty": "intermediate",
        "meta_data": {
            "skills": {"core": ["User Research", "Roadmapping", "Stakeholder Management"], "technical": ["SQL/Analytics", "A/B Testing", "Wireframing"], "soft": ["Communication", "Leadership", "Prioritization"]},
            "tools": ["Jira", "Figma", "Mixpanel / Amplitude", "Notion", "Miro", "SQL"],
            "career_readiness": {"resume": ["Product Case Studies", "MBA / Technical Background"], "interview": ["Product Design", "Metrics", "Estimation"], "portfolio": "Product Tear-Downs / Case Studies"},
            "estimated_time": "6-12 Months",
            "career_progression": ["Associate PM", "PM", "Senior PM", "Group PM", "VP of Product", "CPO"]
        },
        "steps": [
            {"level": "Beginner", "title": "PM Fundamentals", "desc": "What PMs do, product lifecycle, types of PMs (growth, platform, B2B/B2C), and day-in-the-life.", "resources": "Lenny's Newsletter | Shreyas Doshi on Twitter"},
            {"level": "Beginner", "title": "User Research & Empathy", "desc": "User interviews, Jobs-to-be-Done framework, problem statement writing, and building empathy maps.", "resources": "Nielsen Norman Group | Intercom PM Articles"},
            {"level": "Beginner", "title": "Product Discovery & Ideation", "desc": "Opportunity solution trees, brainstorming, concept testing, and hypothesis-driven development.", "resources": "Inspired by Marty Cagan (book)"},
            {"level": "Intermediate", "title": "Roadmapping & Prioritization", "desc": "RICE, ICE, MoSCoW frameworks, OKRs, building roadmaps in Notion/Jira, and communicating to stakeholders.", "resources": "ProductPlan | Atlassian PM Blog"},
            {"level": "Intermediate", "title": "Data & Metrics for PMs", "desc": "Define KPIs, North Star metric, cohort analysis in Amplitude/Mixpanel, and making data-driven decisions.", "resources": "Mixpanel Blog | SQL for Product Managers (Mode)"},
            {"level": "Intermediate", "title": "Working with Engineering & Design", "desc": "Writing PRDs, user stories, sprint planning, backlog grooming, and managing dependencies.", "resources": "Agile Alliance | Google PM Guide"},
            {"level": "Advanced", "title": "Growth & Monetization", "desc": "Acquisition funnels, activation, retention (AARRR), pricing strategies, and growth loops.", "resources": "Reforge (courses) | Andrew Chen's Blog"},
            {"level": "Advanced", "title": "A/B Testing & Experimentation", "desc": "Hypothesis formulation, test design, statistical significance, and post-experiment analysis.", "resources": "Booking.com Experimentation Blog | Evan Miller Tools"},
            {"level": "Advanced", "title": "PM Interview Preparation", "desc": "Product design, product improvement, metrics, estimation, and behavioral questions.", "resources": "Cracking the PM Interview (book) | Exponent (YouTube)"}
        ]
    },

    # ══════════════════════════════════════════════
    # 16. MACHINE LEARNING ENGINEER
    # ══════════════════════════════════════════════
    {
        "title": "Machine Learning Engineer",
        "description": "Bridge the gap between data science and software engineering — build, optimize, and deploy production-grade ML systems at scale.",
        "category": "Data & AI",
        "difficulty": "advanced",
        "meta_data": {
            "skills": {"core": ["Python", "ML Theory", "Software Engineering"], "technical": ["PyTorch/TensorFlow", "Spark", "Docker", "Kubernetes", "MLflow"], "soft": ["Collaboration", "Research Mindset"]},
            "tools": ["VS Code", "Jupyter", "Docker", "Kubernetes", "MLflow", "Airflow"],
            "career_readiness": {"resume": ["Published Models", "Kaggle Medals", "Open Source ML"], "interview": ["ML System Design", "Coding + ML Theory"], "portfolio": "End-to-end ML Pipeline on GitHub"},
            "estimated_time": "12-18 Months",
            "career_progression": ["Junior MLE", "MLE", "Senior MLE", "Staff MLE", "ML Director"]
        },
        "steps": [
            {"level": "Beginner", "title": "Python & Software Engineering Basics", "desc": "OOP, data structures, testing, clean code, type hints, and packaging Python projects.", "resources": "Real Python | Python Docs"},
            {"level": "Beginner", "title": "ML Foundations", "desc": "Supervised, unsupervised learning, gradient descent, bias-variance tradeoff, and model evaluation.", "resources": "Andrew Ng ML Course (Coursera free audit)"},
            {"level": "Beginner", "title": "NumPy, Pandas & Scikit-learn", "desc": "Vectorized computations, data preprocessing pipelines, and building baseline ML models.", "resources": "Kaggle Learn (free)"},
            {"level": "Intermediate", "title": "Deep Learning with PyTorch", "desc": "Tensors, autograd, custom datasets, training loops, CNNs, RNNs, and transfer learning.", "resources": "PyTorch Official Tutorials | fast.ai Part 1"},
            {"level": "Intermediate", "title": "Feature Engineering & Data Pipelines", "desc": "Feature selection, encoding, scaling, handling imbalanced data, and building reproducible pipelines.", "resources": "Hands-On ML (book) | Feature Engineering for ML (O'Reilly)"},
            {"level": "Intermediate", "title": "Experiment Tracking & Model Registry", "desc": "Log experiments with MLflow, compare runs, register and version models, and set baselines.", "resources": "MLflow Docs | Weights & Biases (W&B)"},
            {"level": "Advanced", "title": "Model Deployment & Serving", "desc": "FastAPI REST endpoints, ONNX export, TorchServe, batch vs real-time inference, and latency optimization.", "resources": "BentoML Docs | Seldon Core"},
            {"level": "Advanced", "title": "ML at Scale (Big Data & Distributed Training)", "desc": "PySpark for big data, Horovod/DeepSpeed for distributed training, and GPU cluster management.", "resources": "Databricks Academy | fast.ai Part 2"},
            {"level": "Advanced", "title": "MLOps in Production", "desc": "CI/CD for ML (DVC, CML), model monitoring, data drift detection, canary rollouts, and A/B testing models.", "resources": "Made With ML | Full Stack Deep Learning 2023"}
        ]
    },

    # ══════════════════════════════════════════════
    # 17. SSC CGL (GOVERNMENT JOBS)
    # ══════════════════════════════════════════════
    {
        "title": "SSC CGL (Staff Selection Commission)",
        "description": "Crack the SSC CGL exam to land prestigious Group B & C posts (Income Tax Officer, CBI, Auditor, etc.) in central government departments.",
        "category": "Government",
        "difficulty": "intermediate",
        "meta_data": {
            "skills": {"core": ["Quantitative Aptitude", "English", "Reasoning", "GK"], "technical": ["Computer Basics", "Typing"], "soft": ["Time Management", "Consistency"]},
            "tools": ["Testbook / Gradeup", "SSC Adda247", "Previous Papers", "Newspapers"],
            "career_readiness": {"resume": ["N/A – Exam Based"], "interview": ["N/A – Document Verification Only for most posts"], "portfolio": "N/A"},
            "estimated_time": "6-12 Months",
            "career_progression": ["Tax Assistant", "Inspector Income Tax", "CBI Sub-Inspector", "Assistant Section Officer"]
        },
        "steps": [
            {"level": "Beginner", "title": "Understand SSC CGL Pattern & Posts", "desc": "Study 4 Tiers (Tier 1, 2, 3, 4), post preferences, salary structures, and eligibility.", "resources": "SSC Official Website | Career Launcher Guide"},
            {"level": "Beginner", "title": "Quantitative Aptitude (Tier 1 & 2)", "desc": "Number system, percentage, ratio, time-work, time-speed, geometry, trigonometry, algebra.", "resources": "Rakesh Yadav 7300 Maths | Arihant SSC Maths"},
            {"level": "Beginner", "title": "Reasoning Ability", "desc": "Non-verbal reasoning, pattern series, matrix, coding-decoding, classification, and analogy.", "resources": "MK Pandey | SSC Reasoning PYQs"},
            {"level": "Intermediate", "title": "English Language & Comprehension", "desc": "Grammar rules, one-word substitution, idioms & phrases, fill in blanks, reading comprehension.", "resources": "SP Bakshi English | Neetu Singh English"},
            {"level": "Intermediate", "title": "General Awareness (GK + GS)", "desc": "Static GK (history, geography, polity, science), current events, economy, and sports.", "resources": "Lucent GK | SSC Adda247 Daily GK"},
            {"level": "Intermediate", "title": "Tier 2 Advanced Mathematics", "desc": "Advanced topics: Statistics, Algebra, Geometry, Mensuration, and Data Interpretation.", "resources": "Rakesh Yadav Advance Maths | Paramount SSC"},
            {"level": "Intermediate", "title": "Tier 2 English — Advanced", "desc": "Reading comprehension (long passages), vocabulary, error detection, and sentence improvement.", "resources": "KD Campus | SSC English Capsules"},
            {"level": "Advanced", "title": "Mock Tests & Full-Length Practice", "desc": "Take Tier 1 & Tier 2 mocks daily. Analyze errors, track accuracy, and improve speed.", "resources": "Testbook | Oliveboard SSC CGL Test Series"},
            {"level": "Advanced", "title": "Tier 3 Descriptive & Tier 4 Typing", "desc": "Letter/application/essay writing (250 words), and DEST/CPT typing practice at 2000 key depressions.", "resources": "SSC PYQ Descriptive | Online Typing Tools"}
        ]
    },

    # ══════════════════════════════════════════════
    # 18. STOCK MARKET / PERSONAL FINANCE
    # ══════════════════════════════════════════════
    {
        "title": "Stock Market Investor & Trader",
        "description": "Build long-term wealth and learn to trade profitably. From opening your first demat account to reading financial statements and technical charts.",
        "category": "Finance",
        "difficulty": "beginner",
        "meta_data": {
            "skills": {"core": ["Financial Literacy", "Risk Management"], "technical": ["Technical Analysis", "Fundamental Analysis", "Options Greek"], "soft": ["Patience", "Discipline", "Emotional Control"]},
            "tools": ["Zerodha Kite", "TradingView", "Screener.in", "Moneycontrol", "NSE/BSE Websites"],
            "career_readiness": {"resume": ["NISM Certifications", "Research Reports"], "interview": ["Portfolio Review"], "portfolio": "Documented Trade Journal"},
            "estimated_time": "6-12 Months to competence",
            "career_progression": ["Retail Investor", "Active Trader", "Portfolio Manager (NISM Certified)", "SEBI RIA"]
        },
        "steps": [
            {"level": "Beginner", "title": "Financial Literacy Basics", "desc": "Compound interest, inflation, asset classes (equity, debt, gold, RE), and importance of early investing.", "resources": "Zerodha Varsity Module 1 (free) | PersonalFinanceClub"},
            {"level": "Beginner", "title": "Stock Market Structure", "desc": "NSE/BSE, SEBI, NSDL/CDSL, how trading works, market participants, and opening a demat account.", "resources": "Zerodha Varsity Module 1-2 | NSE India"},
            {"level": "Beginner", "title": "Mutual Funds & Index Investing", "desc": "Equity funds, SIPs, Nifty 50 index funds, expense ratio, NAV, CAGR, and why most SIPs beat active trading.", "resources": "PaisaBazaar | AMFI India | Freefincal"},
            {"level": "Intermediate", "title": "Technical Analysis", "desc": "Candlestick patterns, support/resistance, moving averages, RSI, MACD, and volume analysis.", "resources": "Zerodha Varsity Module 2 | TradingView Docs"},
            {"level": "Intermediate", "title": "Fundamental Analysis", "desc": "Reading annual reports, P/E, P/B, ROCE, ROE, debt ratios, DCF valuation, and sector analysis.", "resources": "Zerodha Varsity Module 3 | Screener.in"},
            {"level": "Intermediate", "title": "Futures & Options Basics", "desc": "Derivatives concepts, call/put options, option chain, hedging, and basic option strategies (covered call).", "resources": "Zerodha Varsity Futures & Options Modules"},
            {"level": "Advanced", "title": "Advanced Options Strategies", "desc": "Straddles, strangles, Iron Condor, calendar spreads, Greeks (Delta, Theta, Vega), and weekly expiry trading.", "resources": "Sensibull | Option Strategies by NSE"},
            {"level": "Advanced", "title": "Portfolio Construction & Risk Management", "desc": "Asset allocation, diversification, position sizing, stop-loss discipline, and portfolio rebalancing.", "resources": "Freefincal | Coffee Can Investing (book)"},
            {"level": "Advanced", "title": "NISM Certifications & Professional Path", "desc": "NISM Series V-A (Mutual Funds), Series VIII (Equity Derivatives), and SEBI Registered Investment Adviser (RIA).", "resources": "NISM.ac.in | SEBI RIA Guidelines"}
        ]
    }
]
