import os
from dotenv import load_dotenv


load_dotenv()


TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN", "")
DEBUG_MODE = os.getenv("DEBUG_MODE", False)

DB_ENGINE = os.getenv("DB_ENGINE", "postgres")
DB_USERNAME = os.getenv("DB_USERNAME", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "green_card")
