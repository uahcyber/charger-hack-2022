#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>
#include <stdint.h>

void setup() {
    setbuf(stdin,0);
    setbuf(stdout,0);
    setbuf(stderr,0);
}

int isLinux() {
    if(access("/bin/sh", F_OK) == 0) {
        return 0;
    }
    return -1;
}

int test() {
    int operator = 0;
    uint64_t opone = 0;
    uint64_t optwo = 0;
    int64_t answer = 0;
    int64_t userInput = 0;
    char operatorTable[2] = {'+','-'};
    for(int i = 0; i < 1000; i++) {
        operator = rand() % 2;
        opone = rand();
        optwo = rand();
        switch(operator) {
            case 0:
                answer = opone + optwo;
                break;
            case 1:
                answer = opone - optwo;
                break;
        }
        printf("%llu %c %llu = ",opone,operatorTable[operator],optwo);
        scanf("%lld",&userInput);
        if (userInput != answer) {
            printf("Wrong!\n");
            return -1;
        }
    }
    printf("You passed! Getting rid of your answers...\n");
    sleep(2);
    system("clear");
    return 0;
}

int main(int argc, char* argv[]) {
    setup();
    char name[32] = {0};
    srand(time(0));
    if(isLinux() != 0) {
        printf("This math homework software only runs on Linux machines!!!");
        return -1;
    }
    printf("=================================================\n");
    printf("Welcome to the worst Math Homework Software ever!\n");
    printf("=================================================\n");
    if(test() != 0) {
        printf("Failed! You failed!\n");
        return -1;
    }
    printf("Congrats! Give us your name so we can submit your excellent score to your professor!\n");
    printf("Name: ");
    fgets(name,64,stdin);
    printf("Again, excellent work %s!\n",name);
    return 0;
}