import requests

def fetch_data(url):
    responce=requests.get(url)
    return responce.json()
