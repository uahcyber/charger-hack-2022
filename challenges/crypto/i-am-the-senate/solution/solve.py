rawdata = "DiDiDiDiDidydydddddyououoouoooevevvvvevverererreerhehheehhhhararrrararthththhhhhetetetetetraraaraaargegeeggeggdyddyyddyyofofffoofoDaDaDaaaaartrrttrrtthPhPPPhhPPlalaaalallgugguugggueieiieiieisTssTTsTssheheeehehhWiWWiiWWiiseseseeeeeItIttIttIthohoooohhouguguggggghthtthhhthnonnoonnnotItIItIIIttsttsststtnonooonnontataaaattastststttttoroorroorrytyttytttyheheehhheeJeJeeeJJeJdidiiiiddiwowooowwwwulullluluudtddttdddteleelleeeelylyylyyylououuuuuou"

data = [rawdata[i:i+10] for i in range(0, len(rawdata), 10)]
flag = ""
for d in data:
    bindata = chr(int(d[2:].replace(d[0],'0').replace(d[1],'1'),2))
    flag += bindata
print(flag)