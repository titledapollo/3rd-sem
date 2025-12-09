#include <stdio.h>
int add(int a, int b) { return a + b; }
int subtract(int a, int b) { return a - b; }
int multiply(int a, int b) { return a * b; }
float divide(int a, int b) { return (float)a / b; }
int main() {
    int choice, x, y;
    do {
        printf("\n--- Calculator Menu ---\n");
        printf("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);
        if (choice >= 1 && choice <= 4) {
            printf("Enter two numbers: ");
            scanf("%d %d", &x, &y);
        }
        switch (choice) {
            case 1: printf("Result = %d\n", add(x, y)); break;
            case 2: printf("Result = %d\n", subtract(x, y)); break;
            case 3: printf("Result = %d\n", multiply(x, y)); break;
            case 4: 
                if (y != 0) 
                    printf("Result = %.2f\n", divide(x, y));
                else 
                    printf("Error: Division by zero!\n");
                break;
            case 5: printf("Exiting...\n"); break;
            default: printf("Invalid choice!\n");
        }
    } while (choice != 5);
    return 0;
}

