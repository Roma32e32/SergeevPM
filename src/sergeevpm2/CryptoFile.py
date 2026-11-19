from aes_bridge import decrypt, encrypt
from pathlib import Path

class CryptoFile:
    def __init__(self, path: str, password: str):
        self.__path =  Path(path)
        self.__password = password

    def read(self) -> str:
        raw = self.__path.read_text(encoding="utf-8")
        decrypted = decrypt(raw, self.__password).decode("utf-8")
        return decrypted

    def write(self, to_write: str):
        encrypted = encrypt(to_write, self.__password).decode("utf-8")
        self.__path.write_text(encrypted, encoding="utf-8")


cf = CryptoFile(r"E:\Roma\PythonProject\SergeevPM\test1.pwm", "12345")
cf.write("123")
print(cf.read())
