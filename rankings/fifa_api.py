from typing import Dict, List
from fifa_rankings_response import FifaRankingsResponse

Rankings = Dict[str, int]


def parse_rankings_from_api(fifa_rankings_response: FifaRankingsResponse) -> Rankings:
    return dict(
        (r["rankingItem"]["name"], r["rankingItem"]["rank"])
        for r in fifa_rankings_response["rankings"]
    )
