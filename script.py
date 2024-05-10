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


token = environ["GH_TOKEN"]
url = f"https://api.github.com/repos/andylolz/github-secrets-test/actions/secrets/SUPER_SECRET"
headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github.v3+json"
}
payload = {
    "encrypted_value": encrypt(environ["PUBLIC_KEY"], "TODO: encrypt it")
}
resp = requests.put(url, headers=headers, json=payload)
resp.raise_for_status()
print(resp.status_code)
