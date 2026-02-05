import os
import sys

# Add the parent directory to sys.path to allow importing app from root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# Vercel needs a variable named 'handler' (or 'app') available in the module
handler = app
