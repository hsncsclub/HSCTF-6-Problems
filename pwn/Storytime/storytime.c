#include <stdio.h>
#include <unistd.h>

void beginning(){
	write(1, "Once upon a time...\n", 40);
}

void middle(){
	write(1, "Middle of story is the best! :D\n", 40);
}

void end(){
	write(1, "The End!\n", 40);
}

int climax(){
	char buffer[40];
	return read(0, &buffer, 4000);
}

int main() {
	char buffer[48];

    setvbuf(stdout, NULL, _IONBF, 0);
    write(1, "HSCTF PWNNNNNNNNNNNNNNNNNNNN\n", 29);
    write(1, "Tell me a story: \n", 18);
    read(0, &buffer, 400);
    return 0;
}