from pmdata import PMData
from conv import data_from_csv, data_to_csv
from aes_bridge import encrypt, decrypt

class PM:
    def __init__(self, file, password):
        self.__file = file
        self.__password = password
        self.__data = data_from_csv(decrypt(file.read()).decode("utf-8"))

    def write_to_file(self):
        csv = data_to_csv(self.__data)
        crypted = encrypt(csv, self.__password)
        self.__file.write(crypted)