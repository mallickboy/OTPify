# Example of usage
import os
from pathlib import Path
from dotenv import load_dotenv

# Get the absolute path of /backend
BASE_DIR = Path(__file__).resolve().parent.parent.parent  

# Load .env from /backend
load_dotenv(BASE_DIR / ".env")

class Settings:
    SECRET_KEY = os.getenv("SECRET_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL")

settings = Settings()