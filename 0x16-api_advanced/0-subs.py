#!/usr/bin/python3
"""A script that returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """A function that returns number of subcribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, allow_redirects=False, headers={"User-Agent": "Chrome/127.0.0"})
    if response.status_code >= 300:
        return 0

    return response.json().get("data").get("subcribers")
