from grabcode.db import get_connection
from grabcode.fetcher import get_media


def save_posts(conn, posts):
    with conn.cursor() as cur:
        for post in posts:
            cur.execute(
                "INSERT INTO posts (id, caption, permalink, timestamp) "
                "VALUES (%s, %s, %s, %s) "
                "ON CONFLICT (id) DO NOTHING",
                (post["id"], post.get("caption"), post["permalink"], post["timestamp"]),
            )


if __name__ == "__main__":
    posts = get_media()["business_discovery"]["media"]["data"]
    with get_connection() as conn:
        save_posts(conn, posts)
