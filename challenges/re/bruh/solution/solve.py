# this challenge is basically brainfuck but with cool, hip phrases the kids these days are using
bfmap = {
    "on god": "+",
    "frfr": "-",
    "no cap": "[",
    "bussin": "]",
    "deadass": ">",
    "sus": "<",
    "yeet": "."
}

with open('../dist/program.fr','r') as fp:
    lines = [x.strip() for x in fp.readlines()]

bf = []
for line in lines:
    bf.append(bfmap[line])
print(''.join(bf))