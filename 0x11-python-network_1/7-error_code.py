#!/usr/bin/python3
"""It sends a request to a given URL and displays the response body.

Usage: ./7-eeror_code.py <URL>
- It handles HTTP errors.
"""
import sys
import requests


if __name__ == "__main__":
    rurl = sys.argv[1]

    r = requests.get(rurl)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
