from grabcode.db import get_connection

with get_connection() as conn:
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id BIGINT UNIQUE NOT NULL,
                caption TEXT,
                permalink TEXT NOT NULL,
                timestamp TIMESTAMPTZ
            )
        """)