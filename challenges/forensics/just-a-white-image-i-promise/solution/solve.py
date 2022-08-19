from PIL import Image

im = Image.open('exfil.png')

data = list(im.getdata())

zip_data = []

for i,j in enumerate(data):
    zip_data.append(f"{255-j[0]:x}")


zip_data = ["".join(zip_data[i:i+2]).zfill(2) for i in range(0,len(zip_data),2)]

with open('solved.zip', 'wb') as f:
    f.write(bytes.fromhex("".join(zip_data)))
