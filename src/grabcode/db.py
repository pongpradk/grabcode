import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

def require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value

def get_connection():
    return psycopg.connect(
        host=require_env("POSTGRES_HOST"),
        port=require_env("POSTGRES_PORT"),
        dbname=require_env("POSTGRES_DATABASE"),
        user=require_env("POSTGRES_USER"),
        password=require_env("POSTGRES_PASSWORD"),
    )