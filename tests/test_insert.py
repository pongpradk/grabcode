import pytest

from grabcode.create_table import create_table
from grabcode.db import get_connection
from grabcode.insert import save_posts


@pytest.fixture
def conn(monkeypatch):
    monkeypatch.setenv("POSTGRES_DATABASE", "grabcode_test")
    with get_connection() as conn:
        create_table(conn)
        conn.execute("TRUNCATE posts")  # every test starts empty
        yield conn


POST = {"id": "1", "permalink": "https://www.instagram.com/DgO4UHCB785/", "timestamp": "2026-11-27T05:01:42+0000"}


def test_saves_post_without_caption(conn):
    save_posts(conn, [POST])

    rows = conn.execute("SELECT id, caption FROM posts").fetchall()

    assert rows == [(1, None)]


def test_saves_duplicate_post(conn):
    save_posts(conn, [POST])
    save_posts(conn, [POST])

    rows = conn.execute("SELECT id, caption FROM posts").fetchall()

    assert rows == [(1, None)]