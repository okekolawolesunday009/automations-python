import requests

p = {"search": "python", "max_results": 10}

response = requests.get("https://api.github.com/search/repositories", params=p)

print(response.url)
print(response.status_code)