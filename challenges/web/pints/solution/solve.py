import requests
from PIL import Image
import numpy as np

pixels = []
width = 432
i = 0
while True:
    print(f'getting {i}')
    r = requests.get(f'http://127.0.0.1:29824/loc/{i}')
    if r.status_code != 200:
        print("end!")
        break
    data = r.text.split('<h1>#')[1].split('</h1>')[0]
    vals = [int(data[i:i+2],16) for i in range(0, len(data), 2)]
    pixels.append(vals)
    i += 1
realPixels = [pixels[i:i+width] for i in range(0, len(pixels), width)]
pixelArray = np.array(realPixels, dtype=np.uint8)
im = Image.fromarray(pixelArray)
im.save('test.png',"PNG")