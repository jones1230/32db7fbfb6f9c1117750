#!/usr/bin/python3
"""Module for 0-subs.py"""


def number_of_subscribers(subreddit):
    """Returns numbers od subs after reddit api query"""
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)

    if response.status_code != 200:
        return (0)
    response = response.json()
    if 'data' in response:
        return (response.get('data').get('subscribers'))

    else:
        return (0)
