#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* xorMessage(const char* message, const char* key) {
    size_t messageLength = strlen(message);
    size_t keyLength = strlen(key);
    char* result = (char*)malloc(messageLength + 1);
    if (result == NULL) {
        perror("Memory allocation failed");
        exit(EXIT_FAILURE);
    }
    for (size_t i = 0; i < messageLength; ++i) {
        result[i] = message[i] ^ key[i % keyLength];
    }
    result[messageLength] = '\0';
    return result;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <secret message>\n", argv[0]);
        return EXIT_FAILURE;
    }

    const char* secretMessage = argv[1];
    const char* key = "\x22\x11\x75\xe1\x66\x12\x0a\x75\xe1\x66";
    char* encryptedMessage = xorMessage(secretMessage, key);

    FILE* outputFile = fopen("enc.txt", "w");
    if (outputFile == NULL) {
        perror("Failed to open file for writing");
        free(encryptedMessage);
        return EXIT_FAILURE;
    }

    fprintf(outputFile, "%s\n", encryptedMessage);

    fclose(outputFile);
    free(encryptedMessage);

    printf("Encrypted message saved to enc.txt\n");
    return EXIT_SUCCESS;
}
