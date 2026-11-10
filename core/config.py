import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Base paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
LANDING_DIR = DATA_DIR / "landing"
PROFILES_DIR = DATA_DIR / "profiles"
STTM_DIR = DATA_DIR / "sttm"
BRONZE_DIR = DATA_DIR / "bronze_layer"
SILVER_DIR = DATA_DIR / "silver_layer"
GOLD_DIR = DATA_DIR / "gold_layer"
REPORTS_DIR = BASE_DIR / "reports"
AUDIT_DIR = BASE_DIR / "audit_logs"
CHROMA_DIR = BASE_DIR / ".chroma"

# LLM Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL = "gemini-2.5-flash"
EMBEDDING_MODEL = "models/text-embedding-004"

# Groq Configuration (preferred - higher free tier limits)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama-3.3-70b-versatile"  # Currently supported Groq model

# GitHub Models Configuration (uses GitHub PAT)
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_MODEL = os.getenv("GITHUB_MODEL", "gpt-4o")

# GitHub Models has two catalog endpoints:
#   - New (2025+):  https://models.github.ai/inference   -> uses prefixed IDs like "openai/gpt-4.1-mini"
#   - Legacy:       https://models.inference.ai.azure.com -> uses bare IDs like "gpt-4o", "gpt-4o-mini"
# We auto-pick based on the model id, but allow explicit override via GITHUB_BASE_URL.
_GITHUB_BASE_URL_ENV = os.getenv("GITHUB_BASE_URL", "").strip()
if _GITHUB_BASE_URL_ENV:
    GITHUB_BASE_URL = _GITHUB_BASE_URL_ENV
elif "/" in (GITHUB_MODEL or ""):
    GITHUB_BASE_URL = "https://models.github.ai/inference"
else:
    GITHUB_BASE_URL = "https://models.inference.ai.azure.com"

# Use Groq if available, else fall back to Gemini
_env_llm = os.getenv("LLM_PROVIDER", "").strip().lower()
if _env_llm in ("groq", "gemini", "github"):
    LLM_PROVIDER = _env_llm
else:
    LLM_PROVIDER = "groq" if GROQ_API_KEY else "gemini"

# Ensure directories exist
for d in [LANDING_DIR, PROFILES_DIR, STTM_DIR, BRONZE_DIR, SILVER_DIR, GOLD_DIR, REPORTS_DIR, AUDIT_DIR, CHROMA_DIR]:
    d.mkdir(parents=True, exist_ok=True)
