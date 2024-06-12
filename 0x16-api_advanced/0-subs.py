#!/usr/bin/python3
"""subscribers count"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'linux:0x16.api.adviced:v1.0.0 (by /u/bdov_)'
            }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = reponse.json().get("data")
    return results.get("subscribers")
