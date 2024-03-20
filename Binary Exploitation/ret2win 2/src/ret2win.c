#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void gadgets() {
    __asm__(
        ".intel_syntax noprefix;"
        "pop rdi; ret;"
        "pop rsi; ret;"
        "pop rdx; ret;"
        ".att_syntax;"
    );
}

void win(long a, long b, long c) {
    char buf[100];
    FILE *fd = fopen("flag.txt", "r");
    if (a != 0xdeadbeefdeadbeef || b != 0xabcd1234dcba4321 || c != 0x147147147147147) {
        printf("No hacking!\n");
        exit(-1);
    }
    if (fd == 0) {
        printf("flag.txt not found\n");
        exit(-1);
    }
    fgets(buf, sizeof(buf), fd);
    fclose(fd);
    printf("Wow, how did you get here? Here's the flag:\n%s\n", buf);
}

int main() {
    char buf[100];
    printf("Give me your payload: ");
    gets(buf);
}

__attribute__((constructor))
void setup(void) {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}
