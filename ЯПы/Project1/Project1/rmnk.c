#include <stdio.h>
#include <stdlib.h>

void encrypt(char* text, int key) {
	for (int i = 0; text[i] != '\0'; i++) {
		char currentChar = text[i];
		if (currentChar >= 'a' && currentChar <= 'z') {
			currentChar = ((currentChar - 'a' + key) % 26) + 'a';
			text[i] = currentChar;
		}
		else if (currentChar >= 'A' && currentChar <= 'Z') {
			currentChar = ((currentChar - 'A' + key) % 26) + 'A';
			text[i] = currentChar;
		}
	}
}

void decrypt(char* text, int key) {
	for (int i = 0; text[i] != '\0'; i++) {
		char currentChar = text[i];
		if (currentChar >= 'a' && currentChar <= 'z') {
			currentChar = ((currentChar - 'a' - key + 26) % 26) + 'a';
			text[i] = currentChar;
		}
		else if (currentChar >= 'A' && currentChar <= 'Z') {
			currentChar = ((currentChar - 'A' - key + 26) % 26) + 'A';
			text[i] = currentChar;
		}
	}
}

int main(int argc, char** argv)
{
	if (argc != 4) {
		printf("Usage: ./caesar <encrypt|decpypt> <string> <key>\n");
		return 1;
	}
	
	char* mode = argv[1];
	char* text = argv[2];
	int key = atoi(argv[3]);

	printf("Source text: %s\n", text);
	printf("Key: %d\n", key);
	
	
	if (strcmp(mode, "encrypt") == 0) {
		encrypt(text, key);
		printf("Encrypted text: %s\n", text);
	}
	else if (strcmp(mode, "decrypt") == 0) {
		decrypt(text, key);
		printf("Decrypted text: %s\n", text);
	}
	else {
		printf("Invalid mode. Use 'encrypt' or 'decrypt'.\n");
		return 1;
	}

	return 0;
}