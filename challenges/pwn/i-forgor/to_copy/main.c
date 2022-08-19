#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

struct playerInfo {
    char name[12];
    int score;
};

void setup() {
    setbuf(stdin,0);
    setbuf(stdout,0);
    setbuf(stderr,0);
}

void menu() {
    printf("==================================\n");
    printf("Welcome to the random score giver!\n");
    printf("==================================\n");
    printf("1. Create player\n2. Delete player\n3. Check if player is a high scorer\n4. Set player score\n5. Re-generate random seed for score selection\nSelection: ");
}

void setPlayerScore(struct playerInfo* pi) {
    int choice = rand() % 11;
    int scores[] = {0, 5, 30, 44, 56, 68, 70, 100, 167, 199, 200};
    pi->score = scores[choice];
    printf("Set %s's score to %d!\n",pi->name,pi->score);
}

struct playerInfo* createPlayer() {
    struct playerInfo* pi = (struct playerInfo*)malloc(0x10);
    if(!pi) {
        printf("Unable to allocate memory for player!!!\n");
        return NULL;
    }
    printf("What is your name?: ");
    scanf("%11s",pi->name);
    setPlayerScore(pi);
    return pi;
}

void checkScore(struct playerInfo* pi) {
    if (pi->score > 200) {
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
        exit(0);
    } else {
        printf("Only high-scorers get flags x)\n");
    }
}

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

int main(int argc, char* argv[]) {
    setup();
    srand(time(0));
    int selection;
    struct playerInfo* pi;
    while (1) {
        menu(); 
        scanf("%d",&selection);
        switch(selection) {
            case 1:
                pi = createPlayer();
                break;
            case 2:
                free(pi);
                break;
            case 3:
                checkScore(pi);
                break;
            case 4:
                setPlayerScore(pi);
                break;
            case 5:
                srand(time(0)+generateSeed());
                break;
            default:
                printf("Invalid selection\n");
                break;
        }
    }
    return 0;
}