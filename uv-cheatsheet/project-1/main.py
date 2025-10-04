# main.py
import requests

def main():
    r = requests.get("https://api.github.com")
    print("Status:", r.status_code)
    print("Some keys:", list(r.json().keys())[:5])

if __name__ == "__main__":
    main()
