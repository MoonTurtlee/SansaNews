import logging
import os
import sys
from pprint import pprint
from typing import Any

import requests
from dotenv import load_dotenv


def main():
    assert len(sys.argv) >= 3, "Not enough arguments"

    ACTIONS = ["check", "get"]
    API_VERSION = "v24.0"
    INSTAGRAM_ID = "17841455210130919"
    API_URL = f"https://graph.facebook.com/{API_VERSION}/{INSTAGRAM_ID}"

    action = sys.argv[1]
    assert action in ACTIONS, f"{action} not in available actions"

    access_token = os.getenv("ACCESS_TOKEN", "")
    assert access_token, "access token is empty"

    if action == "check":
        username = sys.argv[2]
        is_business_account = check_if_business_account(username, API_URL, access_token)
        print(is_business_account)
    elif action == "get":
        username = sys.argv[2]
        posts = get_account_posts(username, API_URL, access_token)
        for post in posts:
            post = sanitize_post(username, post)
        pprint(posts)


def check_if_business_account(
    username: str, url: str, access_token: str, timeout_s: int = 15
) -> bool:
    fields = f"business_discovery.username({username}){{name}}"
    params = {"fields": fields, "access_token": access_token}

    response = None
    try:
        response = requests.get(url, params, timeout=timeout_s)
        response.raise_for_status()
        return response.status_code == 200

    except requests.exceptions.RequestException as error:
        logging.error(f"Could not connect to Instragram API ({error})")
        if response is not None:
            logging.error(response.text)

        return False


def get_account_posts(
    username: str, url: str, access_token: str, amount: int = 5, timeout_s: int = 15
) -> list[dict[str, Any]]:  # pyright: ignore[reportExplicitAny]
    assert amount > 0, "Amount of posts to retrieve must be positive"

    fields = f"""
        business_discovery.username({username}){{
            media.limit({amount}){{
                timestamp,caption,media_type,permalink,media_url,
                children{{media_url,media_type}}
            }}
        }}
    """
    params = {"fields": fields, "access_token": access_token}

    response = None
    try:
        response = requests.get(url, params, timeout=timeout_s)
        response.raise_for_status()
        data = response.json()  # pyright: ignore[reportAny]
        return data["business_discovery"]["media"]["data"]  # pyright: ignore[reportAny]

    except requests.exceptions.RequestException as error:
        logging.error(f"Could not connect to Instagram API ({error})")
        if response is not None:
            logging.error(response.text)

        return []


def sanitize_post(username: str, post: dict[str, Any]):  # pyright: ignore[reportExplicitAny]
    post.pop("id")
    post["username"] = username

    if "children" in post:
        children: list[dict[str, Any]] = post["children"]["data"]  # pyright: ignore[reportExplicitAny,reportAny]
        for child in children:
            child.pop("id")
        post["children"] = children

    return post


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s: [%(levelname)s] %(message)s")
    _ = load_dotenv()
    main()
