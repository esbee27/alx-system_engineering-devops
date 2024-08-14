#!/usr/bin/python3
"""recursive function that queries the Reddit
"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    res = requests.get(url, headers={"User-Agent": "My-Agent"}, params={"count": count, "after": after}, allow_redirects=False)
    if res.status_code >= 400:
        return None
    hot_one = hot_list + [child.get('data').get('title') for child in res.json().get('data').get('children')]
    info = res.json()
    if not info.get('data').get('after'):
        return hot_one
        
    return recurse(subreddit, hot_one, info.get('dta').get('count'), info.get('data').get('after'))
