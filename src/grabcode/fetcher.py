import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_media():
    instagram_user_id = os.getenv("INSTAGRAM_USER_ID")
    extended_user_access_token = os.getenv("EXTENDED_USER_ACCESS_TOKEN")

    URL = f"https://graph.facebook.com/v27.0/{instagram_user_id}?fields=business_discovery.username(grabfoodth){{media.limit(4){{caption,id,permalink,timestamp}}}}&access_token={extended_user_access_token}"

    response = requests.request("GET", URL)

    return response.json()

print(get_media())