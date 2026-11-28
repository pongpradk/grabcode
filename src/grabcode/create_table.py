from grabcode.db import get_connection


def create_table(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id BIGINT UNIQUE NOT NULL,
            caption TEXT,
            permalink TEXT NOT NULL,
            timestamp TIMESTAMPTZ NOT NULL
        )
    """)


if __name__ == "__main__":
    with get_connection() as conn:
        create_table(conn)
