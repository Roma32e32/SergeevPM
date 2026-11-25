from typing import TypedDict


class Record(TypedDict):
    Site: str
    Login: str
    Tags: list[str]
    Password: str

def new_record():
    return Record(Login="", Site="", Tags=[], Password="")