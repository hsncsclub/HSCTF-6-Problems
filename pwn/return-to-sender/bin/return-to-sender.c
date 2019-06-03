#include <stdlib.h>
#include <string.h>
#include <stdio.h>

void win() {
	system("/bin/sh");
}

void vuln() {
	char dest[8];
	printf("Where are you sending your mail to today? ");
	gets(dest);
	printf("Alright, to %s it goes!\n", dest);
}

int main() {
	setbuf(stdout, NULL);
	gid_t gid = getegid();
	setresgid(gid,gid,gid);
	vuln();
	return 0;	
}