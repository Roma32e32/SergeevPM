from crypto_file import CryptoFile

cf = CryptoFile(r'C:\Users\admin\Documents\SergeevPM\test3.pwm', '12345')
cf.write("[{'name': 'Alice', 'age': 271}, {'name': 'Bob', 'age': 22}]")