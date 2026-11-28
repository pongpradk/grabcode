import psycopg
from grabcode.db import conn_info
from grabcode.fetcher import get_media

post = get_media()["business_discovery"]["media"]["data"]

with psycopg.connect(conn_info) as conn:
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO posts (id, caption, permalink, timestamp) VALUES (%s, %s, %s, %s)",
            (post["id"], post.get("caption"), post["permalink"], post["timestamp"]),
        )