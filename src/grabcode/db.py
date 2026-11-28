import psycopg
from dotenv import load_dotenv
from grabcode.config import require_env

load_dotenv()

def get_connection():
    return psycopg.connect(
        host=require_env("POSTGRES_HOST"),
        port=require_env("POSTGRES_PORT"),
        dbname=require_env("POSTGRES_DATABASE"),
        user=require_env("POSTGRES_USER"),
        password=require_env("POSTGRES_PASSWORD"),
    )