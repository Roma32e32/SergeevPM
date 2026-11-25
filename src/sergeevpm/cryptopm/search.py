from rapidfuzz import fuzz, process

from .pmdata import Record


def _record_tags(record: Record) -> list[str]:
    return [tag.strip() for tag in record.tags.split(",") if tag.strip()]


def search_by_site(records: list[Record], site: str) -> list[int]:
    matches = process.extract(
        query=site,
        choices=[record.site for record in records],
        scorer=fuzz.partial_ratio,
        score_cutoff=95,
    )
    return [match[2] for match in matches]


def search_by_login(records: list[Record], login: str) -> list[int]:
    matches = process.extract(
        query=login,
        choices=[record.login for record in records],
        scorer=fuzz.partial_ratio,
        score_cutoff=85,
    )
    return [match[2] for match in matches]


def search_by_tag(records: list[Record], tag: str) -> list[int]:
    matches = [
        process.extract(
            query=tag,
            choices=_record_tags(record),
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
    site: str | None = None,
    login: str | None = None,
    tags: list[str] | None = None,
) -> list[int]:
    found = set(range(len(records)))
    if site is not None:
        found &= set(search_by_site(records, site))
    if login is not None:
        found &= set(search_by_login(records, login))
    if tags is not None:
        found &= set(search_by_tags(records, tags))

    return sorted(found)
