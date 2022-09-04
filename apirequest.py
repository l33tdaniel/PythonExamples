import requests
# nodemon --exec python3 requests.py
response = requests.get("http://randomfox.ca/floof")
fox = response.json()
print(fox)