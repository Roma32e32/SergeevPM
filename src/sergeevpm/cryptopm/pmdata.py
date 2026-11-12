from aes_bridge import encrypt, decrypt
from dataclasses import dataclass


@dataclass
class PMData:
    sites: list[str]
    logins: list[str]
    tags: list[list[str]]
    pwds: list[str]
