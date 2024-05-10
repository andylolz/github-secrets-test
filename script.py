from base64 import b64encode
from os import environ
from nacl import encoding, public
import requests

def encrypt(public_key: str, secret_value: str) -> str:
    """Encrypt a Unicode string using the public key."""
    public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
    sealed_box = public.SealedBox(public_key)
    encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
    return b64encode(encrypted).decode("utf-8")


api_base_url = "https://api.github.com/repos/andylolz/github-secrets-test"
token = environ["GH_TOKEN"]
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github.v3+json"
}

url = f"{api_base_url}/actions/secrets/public-key"
resp = requests.get(url, headers=headers)
resp.raise_for_status()
j = resp.json()
print(j)
public_key = j["key"]


url = f"{api_base_url}/actions/secrets/SUPER_SECRET"
payload = {
    "encrypted_value": encrypt(public_key, "TODO: encrypt it")
}
resp = requests.put(url, headers=headers, json=payload)
resp.raise_for_status()
print(resp.status_code)
