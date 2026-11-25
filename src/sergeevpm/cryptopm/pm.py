from pathlib import Path

from aes_bridge import decrypt, encrypt

from .conv import data_from_csv, data_to_csv
from .pmdata import Record
from .search import search


def check_password(data, password):
    decoded_password = decrypt(data, password).decode("utf-8")
    lines = decoded_password.split("\n")
    return lines[0] == "site;login;tags;pass"


class PM:
    def __init__(self, path, password):
        self.__path = path
        self.__password = password

        decrypted = decrypt(
            Path(path).read_text(encoding="utf-8"), self.__password
        ).decode("utf-8")
        self.records = data_from_csv(decrypted)

    def save(self):
        data = encrypt(data_to_csv(self.records), self.__password)
        Path(self.__path).write_bytes(data)

    def add_record(self):
        self.records.append(Record())
        self.save()

    def find(self, site=None, login=None, tags=None):
        return search(self.records, site, login, tags)
