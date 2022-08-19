import os
import secrets

if not os.path.exists("key"):
    with open("key", "wb") as f:
        f.write(os.urandom(16))

if not os.path.exists("secret"):
    with open("secret", "w") as f:
        f.write(secrets.token_hex(8))