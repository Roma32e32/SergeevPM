from rapidfuzz import fuzz, process
from pmdata import PMData


def search_by_site(data: PMData, site: str) -> list[int]:
    matches = process.extract(query=site, choices=data.sites, scorer=fuzz.partial_ratio, score_cutoff=95)
    matches = [m[2] for m in matches]
    return matches

def search_by_login(data: PMData, login: str) -> list[int]:
    matches = process.extract(query=login, choices=data.logins, scorer=fuzz.partial_ratio, score_cutoff=85)
    matches = [m[2] for m in matches]
    return matches

def search_by_tag(data: PMData, tag: str) -> list[int]:
    matches = process.extract(query=tag, choices=data.tags, scorer=fuzz.partial_ratio, score_cutoff=90)
    matches = [m[2] for m in matches]
    return matches

def search_by_tags(data: PMData, tags: list[str]) -> list[int]:
    pre = [search_by_tag(data, tag) for tag in tags]
    out = set.intersection(*pre)
    return list(out)

def search(data: PMData, site: str, login: str, tags: list[str]) -> list[int]:
    by_site = set(search_by_site(data, site))
    by_login = set(search_by_login(data, login))
    by_tags = set(search_by_tags(data, tags))
    out = by_site & by_login & by_tags
    return list(out)