import math
from rapidfuzz import fuzz, process
from .pmdata import PMData


def search_by_site(data: PMData, site: str) -> list[int]:
    matches = process.extract(query=site, choices=data.sites, scorer=fuzz.partial_ratio, score_cutoff=95)
    matches = [m[2] for m in matches]
    return matches

def search_by_login(data: PMData, login: str) -> list[int]:
    matches = process.extract(query=login, choices=data.logins, scorer=fuzz.partial_ratio, score_cutoff=85)
    matches = [m[2] for m in matches]
    return matches

def search_by_tag(data: PMData, tag: str) -> list[int]:
    matches = [process.extract(query=tag, choices=t, scorer=fuzz.partial_ratio, score_cutoff=90) for t in data.tags]
    out = [i for i, e in enumerate(matches) if e != []]
    return out

def search_by_tags(data: PMData, tags: list[str]) -> list[int]:
    pre = [search_by_tag(data, tag) for tag in tags]
    every = set(list(range(len(data.sites))))
    for e in pre:
        every &= set(e)
    return list(every)

def search(data: PMData, site: str = -1, login: str = -1, tags: list[str] = -1) -> list[int]:
    #by_site = set(search_by_site(data, site))
    #by_login = set(search_by_login(data, login))
    #by_tags = set(search_by_tags(data, tags))

    every = set(list(range(len(data.sites))))
    if site != -1:
        every &= set(search_by_site(data, site))
    if login != -1:
        every &= set(search_by_login(data, login))
    if tags != -1:
        every &= set(search_by_tags(data, tags))

    return list(every)