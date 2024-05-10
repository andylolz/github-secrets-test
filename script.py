from os import environ
import requests


token = environ["GH_TOKEN"]
url = f"https://api.github.com/repos/andylolz/github-secrets-test/actions/secrets/SUPER_SECRET"
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github.v3+json"
}
payload = {
    "encrypted_value": "TODO: encrypt it"
}
resp = requests.put(url, headers=headers, json=payload)
resp.raise_for_status()
print(resp.status_code)
