import requests
import time


time.sleep(2)

response = requests.get("http://server:8000/files/myfile.txt")

if response.status_code == 200:
    print(response.text)
else:
    print(f"Ошибка {response.status_code}")