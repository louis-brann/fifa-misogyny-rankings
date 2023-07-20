#!/usr/bin/env python

import math
from typing import Dict, Optional
import requests
from bs4 import BeautifulSoup

from fifa_rankings_response import FifaRankingsResponse
from fifa_web import parse_rankings_from_webpage
from fifa_api import parse_rankings_from_api

Rankings = Dict[str, int]

# TODO: handle redirecting to most recent results if ?dateId not specified
rankings_config = {
    "women": {
        "api": "https://www.fifa.com/api/ranking-overview?locale=en&dateId=ranking_20230609",
        "web": "https://www.fifa.com/fifa-world-ranking/women?dateId=ranking_20230609",
    },
    "men": {
        "api": "https://www.fifa.com/api/ranking-overview?locale=en&dateId=id14079",
        "web": "https://www.fifa.com/fifa-world-ranking/men?dateId=id14079",
    },
}


def make_request(url: str, referer: Optional[str] = None) -> requests.Response:
    """
    returns content of requests.get

    extra headers needed to avoid \"A critical request has been detected and therefore blocked.\"
    """
    headers = requests.utils.default_headers()
    headers.update(
        {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
            "Referer": referer,
        }
    )
    r = requests.head(url, headers=headers, allow_redirects=True)
    if r.url != url:
        print(f"Redirect detected. Routing to {r.url}")
    url = r.url
    return requests.get(url, headers=headers)


def get_rankings_from_webpage(gender: str) -> Rankings:
    url = rankings_config[gender]["web"]
    page = make_request(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return parse_rankings_from_webpage(soup)


def get_rankings_from_api(gender: str) -> Rankings:
    api_url = rankings_config[gender]["api"]
    web_url = rankings_config[gender]["web"]
    response = make_request(api_url, referer=web_url)
    json: FifaRankingsResponse = response.json()
    return parse_rankings_from_api(json)


def get_rank_diff(womens_rank: int | None, mens_rank: int | None) -> int | float | None:
    if womens_rank and mens_rank:
        rank_diff = mens_rank - womens_rank
    elif not womens_rank:
        rank_diff = math.inf
    elif not mens_rank:
        rank_diff = -math.inf
    else:
        rank_diff = None
    return rank_diff


def calculate_misogyny_rankings(
    womens_rankings: Rankings, mens_rankings: Rankings
) -> Rankings:
    """returns a ranking of most misogynist to least misogynist countries"""
    misogyny_diffs: Rankings = {}
    all_countries = set(womens_rankings.keys()) | set(mens_rankings.keys())
    for country in all_countries:
        womens_rank = womens_rankings.get(country, None)
        mens_rank = mens_rankings.get(country, None)
        misogyny_diffs[country] = get_rank_diff(womens_rank, mens_rank)

    print(f"Misogyny Diffs: {misogyny_diffs}")
    sorted_by_misogyny = sorted(misogyny_diffs.items(), key=lambda i: -1 * i[1])
    print(f"Sorted by Misogyny: {sorted_by_misogyny}")
    return {item[0]: i for i, item in enumerate(sorted_by_misogyny)}


if __name__ == "__main__":
    womens_rankings = get_rankings_from_api("women")
    mens_rankings = get_rankings_from_api("men")

    misogyny_rankings = calculate_misogyny_rankings(womens_rankings, mens_rankings)
    print(misogyny_rankings)
