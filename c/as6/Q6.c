#include <stdio.h>
#include <ctype.h>
void countVowelsConsonants(char str[]) {
    int i, vowels = 0, consonants = 0;
    for (i = 0; str[i] != '\0'; i++) {
        char ch = tolower(str[i]);
        if (ch >= 'a' && ch <= 'z') {
            if (ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u')
                vowels++;
            else
                consonants++;
        }
    }
    printf("Vowels = %d, Consonants = %d\n", vowels, consonants);
}
int main() {
    char str[100];
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    countVowelsConsonants(str);
    return 0;
}

