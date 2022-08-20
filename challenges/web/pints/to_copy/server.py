from flask import Flask, request, render_template, abort
from PIL import Image

app = Flask(__name__)

pixels = None
width = 0

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

@app.before_first_request
def start():
    global pixels
    global width
    im = Image.open('flag.png','r')
    pixels = list(im.getdata())
    width = im.width

@app.route('/')
def home():
    return f"<html><title>Pints</title><body><h1>Pints</h1><br><h3>Check out <a href='/loc/0'>/loc/0</a></h3><br><h4>width: {width}</h4></body></html>"

@app.route('/loc/<number>')
def loc(number):
    number = int(number)
    if number > len(pixels)-1 or number < 0:
        abort(403)
    pixelVals = list(pixels[number])[:-1]
    return f"<html><title>and</title><body><center><h1>{rgb2hex(*pixelVals)}</h1></center></body></html>"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)