import os

# System Paths
INPUT_DIR = "raw_data_intake"
OUTPUT_FILE = "unified_corporate_database.csv"

# API Settings
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
MODEL_NAME = "llama-3.1-8b-instant"
API_URL = "https://api.groq.com/openai/v1/chat/completions"

def validate_config():
    """Ensures the local environment is securely configured before runtime."""
    if not GROQ_API_KEY:
        raise ValueError("[CRITICAL ERROR] GROQ_API_KEY missing from environment memory!")