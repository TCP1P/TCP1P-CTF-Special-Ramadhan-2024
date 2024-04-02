#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char **argv) {
  int seed = time(0);
  srand(seed);

  FILE *flag = fopen(argv[1], "rb");
  if (flag == NULL) {
    printf("Error opening file.\n");
    return 1;
  }
  fseek(flag, 0, SEEK_END);
  int file_len = ftell(flag);
  fseek(flag, 0, SEEK_SET);

  char *content = (char *)malloc(64);
  fread(content, 1, file_len, flag);

  for (int i = 0; i < file_len; i++) {
    int rand1 = rand() & 0xff;
    int rand2 = rand();
    content[i] = content[i] ^ (rand1);
  }

  FILE *flag_enc = fopen(argv[2], "wb");
  fwrite(&seed, 1, 4, flag_enc);
  fwrite(content, 1, file_len, flag_enc);

  printf("Encrypted flag: %s\n", content);

  fclose(flag);
  fclose(flag_enc);
  free(content);
  return 0;
}
