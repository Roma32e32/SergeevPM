from aes_bridge import encrypt, decrypt
from dataclasses import dataclass


def check_password(data, password):
    decoded_password = decrypt(data, password).decode("utf-8")
    lines = decoded_password.split('\n')
    return lines[0] == "site;login;tags;pass"

@dataclass
class PMData:
    sites: list[str]
    logins: list[str]
    tags: list[list[str]]
    pwds: list[str]
