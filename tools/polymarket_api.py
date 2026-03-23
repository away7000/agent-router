import requests

def get_markets(limit=5):
    url = "https://gamma-api.polymarket.com/markets"
    data = requests.get(url).json()
    return data[:limit]
