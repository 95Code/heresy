# --- IMPORTS ---

import sys
import requests
from html.parser import HTMLParser
from urllib.parse import urlparse
import urllib
import json
import re

# --- DOCSTRING ---

"""
This module implements web functionality. 
"""


# --- FUNCTIONS ---

def urlparse(url: str) -> dict:
    o = urllib.parse.urlparse(url)

    data = {
        "scheme": o.scheme,
        "username": o.username,
        "password": o.password,
        "hostname": o.hostname,
        "port": o.port,
        "netloc": o.netloc,
        "path": o.path,
        "params": o.params,
        "query": o.query,
        "fragment": o.fragment,
    }

    return data 


def curl(url: str) -> str:
    try:
        response = requests.get(url)
    except requests.ConnectionError as e:
        raise ValueError("Connection failed.")

    return response.text 


def status(url: str) -> int:
    try:
        response = requests.get(url)
    except requests.ConnectionError as e:
        return 404

    return response.status_code 


def list_urls(html_text: str) -> list:
    hrefs = set() 

    class Parser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag != "a":
                return

            for key, value in attrs:
                if key == "href":
                    hrefs.add(value)
    
    # TODO: Get URLs from script content.
    # TODO: Keep relative URLs.

    Parser().feed(html_text)
    urls = []

    for href in hrefs:
        scheme = urlparse(href)["scheme"]
        if scheme == "https" or scheme == "http":
            urls.append(href)

    return urls


def lsurl(url: str) -> list:
    try:
        text = curl(url)
    except ValueError as e:
        raise ValueError(str(e))

    urls = list_urls(text)
    return urls


# --- SCRIPT ---

if __name__ == "__main__":
    pass

