#!/usr/bin/python3
"""Function returns the number of subscribers for a given valid subreddit"""

def number_of_subscribers(subreddit):
    """Returns numbers od subs after reddit api query"""
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/about.json".format(subreddit),
                            headers={"User-agent": "My-User-Agent"}, allow_redirects=False)
    
    if sub_info.status_code >= 300:
        return 0
    
    return sub_info.json().get("data").get("subscribers")