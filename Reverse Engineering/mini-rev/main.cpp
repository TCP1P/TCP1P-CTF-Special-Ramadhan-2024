#include <iostream>
#include <fstream>
#include <string>

std::string xorMessage(const std::string& message, const std::string& key) {
    std::string result = message;
    int keyLength = key.length();
    for (int i = 0; i < message.length(); ++i) {
        result[i] = message[i] ^ key[i % keyLength];
    }
    return result;
}

int main(int argc, char* argv[]) {
    std::string secretMessage = argv[1];
    std::string key = "\x76\x22\x99\xf2\x11\x67\xfe\x66";
    std::string encryptedMessage = xorMessage(secretMessage, key);
    std::ofstream outputFile("enc.txt");
    if (!outputFile.is_open()) {
        return 1;
    }
    outputFile << encryptedMessage << std::endl;
    outputFile.close();
    return 0;
}
