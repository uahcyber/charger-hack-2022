import base64
import collections
import os
import secrets
import yaml

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from flask import Flask, request

if not os.path.exists("key"):
    with open("key", "wb") as f:
        f.write(os.urandom(16))

if not os.path.exists("secret"):
    with open("secret", "w") as f:
        f.write(secrets.token_hex(8))

KEY = open("key", "rb").read()
SECRET = open("secret", "r").read()
FLAG = "UAH{d0nt_cHe4t_0n_m4th_h0mewoRk}"

with open(__file__) as f:
    MY_SOURCE = f.read().replace(FLAG, "[flag]")

class Calculator():
    def __init__(self, nums):
        self.nums = nums

class MeanCalculator(Calculator):
    def calculate(self):
        return sum(self.nums) / len(self.nums)

class MedianCalculator(Calculator):
    def calculate(self):
        nums = list(sorted(self.nums))
        return nums[int(len(nums) / 2)]

class ModeCalculator(Calculator):
    def calculate(self):
        return collections.Counter(self.nums).most_common()[0][0]

class FlagCalculator(Calculator):
    def calculate(self):
        return FLAG

class NopeCalculator(Calculator):
    def calculate(self):
        return "no lol"

def calculate(obj):
    if isinstance(obj, dict):
        t = {
            "mean": MeanCalculator,
            "median": MedianCalculator,
            "mode": ModeCalculator
        }.get(obj["type"], NopeCalculator)

        obj = t(obj["nums"])

    return str(obj.calculate())

def cipher():
    return Cipher(algorithms.AES(KEY), modes.ECB())

def pad(data):
    while len(data) % 16 != 0:
        data = data + "\x00"

    return data.encode()

def unpad(data):
    return data.rstrip(b"\x00").decode("ascii")

def encrypt(data):
    data = pad(data)

    e = cipher().encryptor()
    return e.update(data) + e.finalize()

def decrypt(data):
    d = cipher().decryptor()
    return unpad(d.update(data) + d.finalize())

def sign(data):
    return encrypt(data + SECRET)

def unsign(data):
    data = decrypt(data)
    if not data.endswith(SECRET):
        raise Exception("Hacker detected")

    return data[:-len(SECRET)]

app = Flask(__name__)

@app.route("/")
def app_index():
    return """
<p>Welcome to the Secure Statistics Service. Using our megaservices-oriented architecture you can quickly and efficiently calculate the mean, median, or mode of any numbers you like in 3 simple steps.
<p>Step 1. Construct some YAML that represents your request. It should look like this:
<pre>{ type: mean, nums: [ 1, 2, 3, 4, 5 ] }</pre>
<p>The <code>type</code> can be <code>mean</code>, <code>median</code>, or <code>mode</code>.
<p>Step 2. POST your request to <code>/sign/</code> to get a secure request token.
<p>Step 3. POST your secure request token to <code>/calculate/</code> to get the result.
<p>Easy, fast, efficient, and secure. So secure, in fact, that we publish our source code so you can verify there are no security vulnerabilities:
<pre>""" + MY_SOURCE

@app.route("/encrypt/", methods=["POST"])
def app_encrypt():
    # FOR DEBUGGING ONLY - REMOVE IN PRODUCTION!!!!!
    data = request.get_data().decode()
    return base64.b64encode(encrypt(data)).decode()

@app.route("/sign/", methods=["POST"])
def app_sign():
    data = request.get_data().decode()
    if "!" in data:
        return "Hacker detected"

    return base64.b64encode(sign(data)).decode()

@app.route("/calculate/", methods=["POST"])
def app_calculate():
    data = base64.b64decode(request.get_data().decode())

    try:
        data = unsign(data)
    except Exception:
        return "Hacker detected"

    data = yaml.unsafe_load(data)
    return calculate(data)


app.run(host='0.0.0.0', debug=False, port=5000)
