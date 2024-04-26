import requests

min_len = 3
max_len = 8
url = f"https://uzby.com/api.php?min={min_len}&max={max_len}"

response = requests.get(url)
print(response.text)