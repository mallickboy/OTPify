# App configurations (database, email settings)

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
    MASTER_EMAIL_ID=os.getenv("MASTER_EMAIL_ID")
    MASTER_EMAIL_PASSWORD=os.getenv("MASTER_EMAIL_PASSWORD")
    MASTER_EMAIL_ALIAS=os.getenv("MASTER_EMAIL_ALIAS")

settings = Settings()

# print(settings.MASTER_EMAIL_ID)