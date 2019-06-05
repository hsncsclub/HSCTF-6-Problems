#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define WORDS_MAX 370100

char *flag;

typedef struct {
  char *w;
  int len;
} word;

void learn(word a);
void stdinflush();

word dict[WORDS_MAX];
int wc;
word opt[26][26][26];
#define optc(a,b,c) opt[a-'a'][b-'a'][c-'a']

int main(void) {
  setvbuf(stdout, NULL, _IONBF, 0);
  FILE *fflag = fopen("flag.txt", "r");
  fscanf(fflag, "%s", flag);
  FILE *fw = fopen("words.txt", "r");
  if (fw == NULL) {
    perror("fopen");
    exit(EXIT_FAILURE);
  }
  printf("Dictionary opened.\n");
  size_t len = 0;
  while ((dict[wc].len = getline(&dict[wc].w, &len, fw)) != -1) {
    if (dict[wc].w[dict[wc].len-1] == '\n')
      dict[wc].w[--dict[wc].len] = '\0';
    ++wc, len = 0;
  }
  printf("Dictionary scanned. wc: %d\n", wc);
  for (int i = 0; i < wc; ++i)
    learn(dict[i]);
  printf("Preproccessed.\n");
  while (1) {
    char s[4];
    fgets(s, 4, stdin);
    stdinflush();
    word res = optc(s[0],s[1],s[2]);
    printf(res.w ? "%s (%d)\n" : "No words found!\n", res.w, res.len);
  }
}

void learn(word a) {
  for (int i = 0; i < a.len - 2; ++i) {
    if (optc(a.w[i],a.w[i+1],a.w[i+2]).len < a.len)
      optc(a.w[i],a.w[i+1],a.w[i+2]) = a;
  }
}

void stdinflush() {
  int c;
  while ((c = getchar()) != '\n' && c != EOF);
}
