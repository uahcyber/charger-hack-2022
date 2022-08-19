#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void setup() {
    setbuf(stdin,0);
    setbuf(stdout,0);
    setbuf(stderr,0);
}

void printFlag() {
    FILE* fp = fopen("flag.txt","r");
    if(!fp) {
        printf("Unable to open flag!\n");
        exit(-1);
    }
    fseek(fp,0,SEEK_END);
    long fsize = ftell(fp);
    fseek(fp,0,SEEK_SET);
    char* flag = (char*)malloc(fsize+1);
    if(!flag) {
        printf("Could not allocate memory for flag!\n");
        exit(-1);
    }
    fread(flag,1,fsize,fp);
    printf("flag: %s\n",flag);
    free(flag);
}

void play(char* board) {
    for(int i = 0; i < 9; i++) {
        if (board[i] == ' ') {
            board[i] = 'o';
            break;
        }
    }
}

int isWin(char* board) {
    // check three in a row
    for(int i = 0; i < 9; i+=3) {
        if (board[i] != ' ' && board[i] == board[i+1] && board[i] == board[i+2]) {
            if (board[i] == 'x')
                return 1; // x wins
            else
                return 2; // o wins
        }
    }
    // check three in column
    for(int i = 0; i < 3; i++) {
        if(board[i] != ' ' && board[i] == board[i+3] && board[i] == board[i+6]) {
            if (board[i] == 'x')
                return 1; // x wins
            else
                return 2; // o wins
        }
    }
    // check diagonals
    // l-r
    if (board[0] != ' ' && board[0] == board[4] && board[0] == board[8]) {
        if (board[0] == 'x')
            return 1; // x wins
        else
            return 2; // o wins
    }
    // r-l
    if (board[2] != ' ' && board[2] == board[4] && board[2] == board[6]) {
        if (board[2] == 'x')
            return 1; // x wins
        else
            return 2; // y wins
    }
    return 0; // no one wins
}

void printBoardSelection() {
    printf("0 | 1 | 2\n---------\n3 | 4 | 5\n---------\n6 | 7 | 8\n");
}

void printBoard(char* board) {
    printf("Current board:\n");
    for(int i = 0; i < 9; i+=3) {
        printf("%c | %c | %c\n",board[i],board[i+1],board[i+2]);
        if (i != 6) {
            printf("---------\n");
        }
    }
}

int main(int argc, char* argv[]) {
    setup();
    int selection = 0;
    int admin = 0;
    char board[9] = {' ',' ',' ',' ',' ',' ',' ',' ',' '};
    printf("Welcome to TicTacToe!\nInput a board location to place your 'x'.\n");
    while(1) {
        printBoard(board);
        printf("\n");
        printBoardSelection();
        printf("Selection (0-8): ");
        scanf("%d",&selection);
        if (board[selection] == 'x' || board[selection] == 'o') {
            printf("Board location %d is taken!\n",selection);
            continue;
        }
        board[selection] = 'x';
        int won = isWin(board);
        if (won != 0) {
            printBoard(board);
            if (won == 1) {// x wins, check admin
                printf("you win!!\n");
                if (admin != 0) {
                    printFlag();
                }
            } else {
                printf("you lose!\n");
            }
            break;
        }
        play(board);
    }
    return 0;
}