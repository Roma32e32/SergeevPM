from rapidfuzz import fuzz, process
from .record import Record
from typing import Never


def search_by_site(records: list[Record], site: str) -> list[int]:
    matches = process.extract(
        query=site,
        choices=[record['Site'] for record in records],
        scorer=fuzz.partial_ratio,
        score_cutoff=95
    )
    return [match[2] for match in matches]


def search_by_login(records: list[Record], login: str) -> list[int]:
    matches = process.extract(
        query=login,
        choices=[record['Login'] for record in records],
        scorer=fuzz.partial_ratio,
        score_cutoff=85,
    )
    return [match[2] for match in matches]


def search_by_tag(records: list[Record], tag: str) -> list[int]:
    matches = [
        process.extract(
            query=tag,
            choices=record['Tags'],
            scorer=fuzz.partial_ratio,
            score_cutoff=90,
        )
        for record in records
    ]
    return [index for index, match in enumerate(matches) if match]


def search_by_tags(records: list[Record], tags: list[str]) -> list[int]:
    found = set(range(len(records)))
    for tag in tags:
        found &= set(search_by_tag(records, tag))
    return list(found)


def search(
    records: list[Record],
    site: str = '',
    login: str = '',
    tags: list[str] | list[Never] = [],
) -> list[int]:
    found = set(range(len(records)))
    if site != '':
        found &= set(search_by_site(records, site))
    if login != '':
        found &= set(search_by_login(records, login))
    if tags != []:
        found &= set(search_by_tags(records, tags))

    return sorted(found)
