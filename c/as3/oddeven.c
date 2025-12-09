#include <stdio.h>

int main()
{
    int a;
    printf("Enter any number: ");
    scanf("%d", &a);

    if (a % 2 == 0)
    {
        printf("is even\n");
    }
    else
    {
        printf("is odd\n");
    }

    return 0;
}
