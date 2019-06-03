#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <errno.h>

void flag();
void flip(unsigned long bit, unsigned short int offset);

void flag() {
    FILE *f;
    char s;

    printf("[🛐] pwn gods like you deserve this: ");

    f = fopen("flag.txt", "r");

    while((s = fgetc(f)) != EOF) {
        printf("%c", s);
    }

    fclose(f);

    exit(0);
}

void flip(unsigned long bit, unsigned short int offset) {
    unsigned long *b = (void*) (unsigned long) bit;
    unsigned short int val = *b;
    
    *b ^= 1UL << offset;
    printf("Here's your new byte: %x\n", *b);

    return;
}

int main(unsigned long argc, char **argv) {
    setvbuf(stdout, NULL, _IONBF, 0);

    char input[10];

    printf("Welcome to the bit.\n\nNo nonsense, just pwn this binary. You have 4 tries. Live up to kmh's expectations, and get the flag.\n\n");

    for(int i = 0; i < 4; i++) {
        printf("Give me the address of the byte: ");
        fgets(input, 10, stdin);
        unsigned long decoded = (unsigned long) strtoul(input, NULL, 16);

        errno = 0;
        if (errno == ERANGE) {
            printf("Lol, try again (hex uint32).");
            exit(1);
        } else {
            printf("Give me the index of the bit: ");
            fgets(input, 10, stdin);
            unsigned short int offset = (unsigned short int) strtol(input, NULL, 10);

            if(offset < 0 || offset > 7) {
                printf("Try again.");
                exit(1);
            }

            printf("Took care of %08x at offset %d for ya.\n\n", decoded, offset);

            flip(decoded, offset);
        }
    }

    printf("Well, at least you tried.\n");
    exit(0);
}
