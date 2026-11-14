import os

import requests
from dotenv import load_dotenv

load_dotenv()

GRAPH_API_URL = "https://graph.facebook.com/v27.0"
FIELDS = "business_discovery.username(grabfoodth){media.limit(4){caption,id,permalink,timestamp}}"


def get_media():
    instagram_user_id = os.getenv("INSTAGRAM_USER_ID")
    extended_user_access_token = os.getenv("EXTENDED_USER_ACCESS_TOKEN")

    response = requests.get(
        f"{GRAPH_API_URL}/{instagram_user_id}",
        params={"fields": FIELDS, "access_token": extended_user_access_token},
        timeout=5,
    )
    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    print(get_media())
