#include <stdlib.h>
#include <string.h>
#include <stdio.h>

void vuln() {
	char dest[8];
	printf("Dude you hear about that new game called /bin/sh");
	printf("? Enter the right combo for some COMBO CARNAGE!: ");
	gets(dest);
}

int main() {
	setbuf(stdout, NULL);
	gid_t gid = getegid();
	setresgid(gid,gid,gid);
	vuln();
	return 0;	
}