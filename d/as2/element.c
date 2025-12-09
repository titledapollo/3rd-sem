#include <stdio.h>

int main() {
    int arr[100], n, i, pos, element, choice;

    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);

    if (n > 100 || n < 0) {
        printf("Invalid size!\n");
        return 1;
    }

    printf("Enter %d elements:\n", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    if (n >= 100) {
        printf("Array is full. Cannot insert more elements.\n");
        return 1;
    }

    printf("\nWhere do you want to insert the element?\n");
    printf("1. At the beginning\n");
    printf("2. At the end\n");
    printf("3. At any position\n");
    printf("Enter your choice (1/2/3): ");
    scanf("%d", &choice);

    printf("Enter the element to insert: ");
    scanf("%d", &element);

    switch(choice) {
        case 1:
            for (i = n; i > 0; i--) {
                arr[i] = arr[i - 1];
            }
            arr[0] = element;
            n++;
            break;

        case 2:
            arr[n] = element;
            n++;
            break;

        case 3:
            printf("Enter the position (1 to %d): ", n + 1);
            scanf("%d", &pos);

            if (pos < 1 || pos > n + 1) {
                printf("Invalid position!\n");
                return 1;
            }

            for (i = n; i >= pos; i--) {
                arr[i] = arr[i - 1];
            }
            arr[pos - 1] = element;
            n++;
            break;

        default:
            printf("Invalid choice!\n");
            return 1;
    }

    printf("Array after insertion:\n");
    for (i = 0; i < n; i++) {
        printf("%d\n", arr[i]);
    }

    return 0;
}

