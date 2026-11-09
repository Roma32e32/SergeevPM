import os
import base64
from aes_bridge import encrypt, decrypt
from aes_bridge import  encrypt_gcm_bin, decrypt_gcm_bin

def check_password(data, password):
    decoded_password = decrypt(data, password).decode("utf-8")
    lines = decoded_password.split('\n')
    return lines[0] == "site;login;tags;pass"




#file1 = open(r"E:\Roma\PythonProject\SergeevPM\test2.bin", "r")
#data1 = file1.read()
#data2 = decrypt(data1, "12345")
#print(data2)

#print(check_password(data1, "12345"))

#file1.close()


class CryptedPM:
    def __init__(self, file, password):
        pass
