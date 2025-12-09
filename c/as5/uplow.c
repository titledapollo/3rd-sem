#include <stdio.h>

int main() {
    char str[100];
    int i;

    printf("Enter a string: ");
    scanf(" %[^\n]", str);  // Accepts spaces

    printf("Uppercase: ");
    for (i = 0; str[i] != '\0'; i++) {
        if (str[i] >= 'a' && str[i] <= 'z') {
            printf("%c", str[i] - 32); 
        } else {
            printf("%c", str[i]);
        }
    }

    printf("\nLowercase: ");
    for (i = 0; str[i] != '\0'; i++) {
        if (str[i] >= 'A' && str[i] <= 'Z') {
            printf("%c", str[i] + 32);
        } else {
            printf("%c", str[i]);
        }
    }

    printf("\n");
    return 0;
}

