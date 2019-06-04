#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <errno.h>
#include <signal.h>

void flag();
void handler();
void flip(unsigned long byte);

void flag() {
    FILE *f;
    char s;

    printf("that was easy, right? try the next level (bit). here's your flag: ");

    f = fopen("flag", "r");

    while((s = fgetc(f)) != EOF) {
        printf("%c", s);
    }

    fclose(f);

    exit(0);
}

void handler() {
    printf("Something didn't go right (segfault).");

    return;
}

void zero(unsigned long byte) {
    unsigned long *b = (void*) (unsigned long) byte;
    unsigned char val = *b;
    
    *b = 0;

    return;
}

int main(unsigned long argc, char **argv) {
    setvbuf(stdout, NULL, _IONBF, 0);

    signal(SIGSEGV, SIG_IGN);

    char input[100];
    unsigned short int isnormaluser;

    isnormaluser = 0x1;

    printf("Welcome to the byte.\n\nI'll give you a couple tries on this one.\n\n");

    for(int i = 0; i < 2; i++) {
        printf("Give me the address of the byte: ");
        fgets(input, 10, stdin);
        unsigned long decoded = (unsigned long) strtoul(input, NULL, 16);
        input[strcspn(input, "\n")] = 0;

        errno = 0;
        if (errno == ERANGE) {
            printf("Lol, try again (hex uint32).");
            exit(1);
        } else if (input[0] != "f"[0]) {
            // do a crappy check thing
            strcat(input, " is not a valid pointer (must start with `f`. Try again.)\n\n");

            printf(input);
        } else {
            int test;
            test = &test;

            strcat(input, " has been nullified!\n\n");

            printf(input);

            zero(decoded);
        }
    }
    
    if(!isnormaluser) {
        flag();
    } else {
        printf("Well, at least you tried.\n");
    }
    exit(0);
}
