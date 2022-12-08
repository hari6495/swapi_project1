import requests
from pprint import pprint
from utils.randgen import randgen
foo= randgen()
chars=[]
for i in foo:
    chars.append(i)

url = "https://swapi.dev/api/people/{0}"
for c in chars:
    char_url = url.format(c)
    response = requests.get(char_url)
    print(f"fetching details from {char_url} =>\n")
    data = response.json()
    pprint(data)
    print("-------" * 20)
