#include <stdio.h>

int main()
{
    int num1, num2;

    printf("Enter two numbers: ");
    scanf("%d%d", &num1, &num2);

    if (num1 > num2)
    {
        printf("%d is maximum\n", num1);
    }

    if (num2 > num1)
    {
        printf("%d is maximum\n", num2);
    }

    if (num1 == num2)
    {
        printf("Both are equal\n");
    }

    return 0;
}
