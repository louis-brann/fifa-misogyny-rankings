from typing import List, TypedDict


class FifaRankingsResponse(TypedDict):
    rankings: List["FifaRanking"]


class FifaRanking(TypedDict):
    rankingItem: "FifaRankingItem"
    previousPoints: float
    tag: "FifaTag"


class FifaRankingItem(TypedDict):
    rank: int
    flag: "FifaFlag"
    name: str
    totalPoints: float
    active: bool
    previousRank: int
    countryURL: str
    countryCode: str


class FifaFlag(TypedDict):
    src: str
    width: int
    height: int
    title: str
    alt: str


class FifaTag(TypedDict):
    id: str
    text: str
