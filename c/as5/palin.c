#include <stdio.h>
#include <string.h>

int main() {
    char str[100], reversed[100];
    int length, i, isPalindrome = 1;

    printf("Enter a string: ");
    scanf("%s", str);

    length = strlen(str);

    for (i = 0; i < length; i++) {
        reversed[i] = str[length - i - 1];
    }
    reversed[length] = '\0';  

    for (i = 0; i < length; i++) {
        if (str[i] != reversed[i]) {
            isPalindrome = 0;
            break;
        }
    }

    if (isPalindrome)
        printf("The string \"%s\" is a palindrome.\n", str);
    else
        printf("The string \"%s\" is not a palindrome.\n", str);

    return 0;
}

