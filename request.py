import requests
import os
from dotenv import load_dotenv

load_dotenv()

instagram_user_id = os.getenv("INSTAGRAM_USER_ID")
extended_user_access_token = os.getenv("EXTENDED_USER_ACCESS_TOKEN")

url = f"https://graph.facebook.com/v27.0/{instagram_user_id}?fields=business_discovery.username(grabfoodth){{media.limit(4){{caption,id,permalink,timestamp}}}}&access_token={extended_user_access_token}"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
