import base64
import requests

def sign(data):
    return requests.post("http://localhost:19813/sign/", data=data).text

def encrypt(data):
    return requests.post("http://localhost:19813/encrypt/", data=data).text

def calculate(data):
    return requests.post("http://localhost:19813/calculate/", data=data).text

def brute_one(n, prev=[]):
    # gets the nth-to-last character of the secret
    # by constructing all possible blocks it might be, and comparing

    # what we are looking for - last block only
    req = "x" * (n + 1)
    target = base64.b64decode(sign(req))[-16:]

    # now find a match
    prev = "".join(prev)

    possibles = "0123456789abcdef"
    for possible in possibles:
        this = base64.b64decode(encrypt(possible + prev))[-16:]
        if this == target:
            return possible

data = []
for i in range(16):
    print(data)
    data.insert(0, brute_one(i, data))

data = "".join(data)
print("got secret", data)

token = encrypt("!!python/object/new:__main__.FlagCalculator { nums: null }" + data)
print(calculate(token))
