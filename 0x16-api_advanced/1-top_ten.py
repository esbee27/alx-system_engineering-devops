#!/usr/bin/python3
"""A script that queries the Reddit API and prints the titles of the first 10 hot"""
import requests


def top_ten(subreddit):
    """a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    res = requests.get(url, allow_redirects=False)
    if res.status_code == 200:
        for post in res.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)
