import pytest
import requests
import responses
from responses import matchers

from grabcode.fetcher import get_media

URL = "https://graph.facebook.com/v27.0/123"

MEDIA_RESPONSE = {
    "business_discovery": {
        "media": {
            "data": [
                {
                    "caption": "Code 'FOODIE'",
                    "id": "18130983143489491",
                    "permalink": "https://www.instagram.com/p/DfmRR5KEmAP/",
                    "timestamp": "2026-11-11T10:30:03+0000",
                },
                {
                    "caption": "Code 'GUBONUS'",
                    "id": "28130983143489491",
                    "permalink": "https://www.instagram.com/p/AfmRR5KEmAP/",
                    "timestamp": "2026-11-11T10:02:40+0000",
                },
                {
                    "id": "38130983143489491",
                    "permalink": "https://www.instagram.com/p/BfmRR5KEmAP/",
                    "timestamp": "2026-11-11T09:15:00+0000",
                },
            ]
        }
    }
}


@pytest.fixture(autouse=True)
def env(monkeypatch):
    monkeypatch.setenv("INSTAGRAM_USER_ID", "123")
    monkeypatch.setenv("EXTENDED_USER_ACCESS_TOKEN", "test-token")


@responses.activate
def test_get_media_returns_parsed_json():
    responses.get(
        URL,
        json=MEDIA_RESPONSE,
        match=[
            matchers.query_param_matcher(
                {
                    "fields": "business_discovery.username(grabfoodth){media.limit(4){caption,id,permalink,timestamp}}",
                    "access_token": "test-token",
                }
            )
        ],
    )

    assert get_media() == MEDIA_RESPONSE


@responses.activate
def test_get_media_raises_on_http_error():
    responses.get(URL, status=400)

    with pytest.raises(requests.HTTPError):
        get_media()


@responses.activate
def test_get_media_raises_on_timeout():
    responses.get(URL, body=requests.Timeout())

    with pytest.raises(requests.Timeout):
        get_media()


def test_get_media_raises_on_missing_env(monkeypatch):
    monkeypatch.delenv("INSTAGRAM_USER_ID")

    with pytest.raises(RuntimeError, match="INSTAGRAM_USER_ID"):
        get_media()
