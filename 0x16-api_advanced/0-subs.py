#!/usr/bin/python3
"""A script thatreturns the number of subscribers"""

import requests

def number_of_subscribers(subreddit):
    """A function that returns number of subcribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, allow_redirects=False)
    if response.status_code == 200:
        return response.json()['data']['subcribers']
    return 0
