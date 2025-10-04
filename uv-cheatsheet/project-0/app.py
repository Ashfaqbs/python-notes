import requests
r = requests.get("https://api.github.com")
print("Status:", r.status_code)
print("Headers:", list(r.headers.keys())[:5])