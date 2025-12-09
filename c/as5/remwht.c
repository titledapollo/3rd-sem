#include <stdio.h>

int main() {
    char str[200], result[200];
    int i = 0, j = 0;

    printf("Enter a string: ");
    scanf(" %[^\n]", str);

    while (str[i] != '\0') {
        if (str[i] != ' ' && str[i] != '\t' && str[i] != '\n') {
            result[j++] = str[i];
        }
        i++;
    }

    result[j] = '\0';

    printf("String without whitespace: %s\n", result);

    return 0;
}

