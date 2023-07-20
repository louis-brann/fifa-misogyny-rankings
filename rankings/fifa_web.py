from bs4 import BeautifulSoup, PageElement, ResultSet

from typing import Dict, Tuple

Rankings = Dict[str, str]


def parse_rankings_from_webpage(soup: BeautifulSoup) -> Rankings:
    # TODO this only handles the first page

    rankings: Rankings = {}

    RANKING_TABLE_CLASS = "table_rankingTable"
    ranking_table_selector = f"table[class*={RANKING_TABLE_CLASS}]"
    results: ResultSet = soup.select(ranking_table_selector)
    if not results:
        raise Exception(
            f"Error finding ranking table. Found {results} for selector {ranking_table_selector}."
        )
    ranking_table: PageElement = results[0]

    RANKING_ROW_CLASS = "row_rankingTableFullRow"
    ranking_row_selector = f"tr[class*={RANKING_ROW_CLASS}]"
    rows = ranking_table.select(ranking_row_selector)
    for row in rows:
        country, rank = extract_country_rank_from_row(row)
        rankings[country] = rank

    return rankings


def extract_country_rank_from_row(row: PageElement) -> Tuple[str, int]:
    # aria-label e.g. "1 USA" . we just need the country so we split + grab second
    if "aria-label" not in row:
        raise Exception(
            "Row missing aria-label attribute. Can't extract country + rank"
        )
    aria_label = row["aria-label"]
    rank, country = aria_label.split(" ")
    return country, rank
