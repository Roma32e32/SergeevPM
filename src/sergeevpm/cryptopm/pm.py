from pmdata import PMData
from conv import data_from_csv, data_to_csv
from aes_bridge import encrypt, decrypt
from search import search

def check_password(data, password):
    decoded_password = decrypt(data, password).decode("utf-8")
    lines = decoded_password.split('\n')
    return lines[0] == "site;login;tags;pass"


class PM:
    def __init__(self, file, password):
        self.__file = file
        self.__password = password

        raw = self.__file.read()
        decrypted = decrypt(raw, self.__password).decode("utf-8")
        data = data_from_csv(decrypted)
        self.__data = data

    def ___write_to_file(self):
        csv = data_to_csv(self.__data)
        crypted = encrypt(csv, self.__password)
        self.__file.write(crypted)

    def set_site(self, i, new_site):
        self.__data.sites[i] = new_site
        self.___write_to_file()

    def set_login(self, i, new_login):
        self.__data.logins[i] = new_login
        self.___write_to_file()

    def set_tags(self, i, new_tags):
        self.__data.tags[i] = new_tags.split(",")
        self.___write_to_file()

    def set_pass(self, i, new_pass):
        self.__data.pwds[i] = new_pass
        self.___write_to_file()

    def get_record(self, i):
        return self.__data.sites[i], self.__data.logins[i], self.__data.tags[i], self.__data.pwds[i]

    def find(self, site=-1, login=-1, tags=-1):
        return search(self.__data, site, login, tags)