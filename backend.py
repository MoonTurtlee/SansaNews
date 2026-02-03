import os
import sys

import requests
from dotenv import load_dotenv


def check_if_business_account(username: str, url: str, access_token: str) -> bool:
    fields = f"business_discovery.username({username}){{name}}"
    params = {
        "fields": fields,
        "access_token": access_token,
    }

    response = requests.get(url, params)
    is_business_account = response.status_code == 200
    return is_business_account


if __name__ == "__main__":
    API_VERSION = "v24.0"
    INSTAGRAM_ID = "17841455210130919"
    API_URL = f"https://graph.facebook.com/{API_VERSION}/{INSTAGRAM_ID}"

    _ = load_dotenv()
    access_token = os.getenv("ACCESS_TOKEN", "")
    assert access_token, "access token is empty"

    action = sys.argv[1]

    if action == "check":
        username = sys.argv[2]
        is_business_account = check_if_business_account(username, API_URL, access_token)
        print(is_business_account)
