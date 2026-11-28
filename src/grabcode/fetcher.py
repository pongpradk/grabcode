import json

import requests
from dotenv import load_dotenv
from grabcode.config import require_env

GRAPH_API_URL = "https://graph.facebook.com/v27.0"
DEFAULT_LIMIT = 1


def build_fields(limit: int) -> str:
    return (
        "business_discovery.username(grabfoodth)"
        f"{{media.limit({limit}){{caption,id,permalink,timestamp}}}}"
    )


def get_media(limit: int = DEFAULT_LIMIT):
    instagram_user_id = require_env("INSTAGRAM_USER_ID")
    extended_user_access_token = require_env("EXTENDED_USER_ACCESS_TOKEN")

    response = requests.get(
        f"{GRAPH_API_URL}/{instagram_user_id}",
        params={"fields": build_fields(limit), "access_token": extended_user_access_token},
        timeout=5,
    )
    if not response.ok:
        try:
            message = response.json()["error"]["message"]
        except (ValueError, KeyError, TypeError):
            response.raise_for_status()
        raise requests.HTTPError(
            f"Graph API error {response.status_code}: {message}", response=response
        )

    return response.json()


if __name__ == "__main__":
    load_dotenv()
    print(json.dumps(get_media(), ensure_ascii=False, indent=2))
