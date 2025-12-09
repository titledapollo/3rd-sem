#include <stdio.h>
#include <stdlib.h>
#define MAX 100

typedef struct {
    int data[MAX];
    int top;
} Stack;

void push(Stack* s);
void pop(Stack* s);
void display(Stack* s);

int main() {
    int numStacks, choice, stackNum;
    
    printf("Enter the number of stacks: ");
    scanf("%d", &numStacks);

    if (numStacks <= 0 || numStacks > 100) {
        printf("Invalid number of stacks.\n");
        return 1;
    }
    Stack* stacks = (Stack*)malloc(numStacks * sizeof(Stack));
    for (int i = 0; i < numStacks; i++) {
        stacks[i].top = -1;
    }
    while (1) {
        printf("\nChoose operation:\n");
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        if (choice == 4) break;

        printf("Enter stack number (0 to %d): ", numStacks - 1);
        scanf("%d", &stackNum);

        if (stackNum < 0 || stackNum >= numStacks) {
            printf("Invalid stack number.\n");
            continue;
        }
        switch (choice) {
            case 1:
                push(&stacks[stackNum]);
                break;
            case 2:
                pop(&stacks[stackNum]);
                break;
            case 3:
                display(&stacks[stackNum]);
                break;
            default:
                printf("Invalid choice.\n");
        }
    }
    free(stacks);
    return 0;
}
void push(Stack* s) {
    if (s->top == MAX - 1) {
        printf("Stack overflow!\n");
        return;
    }
    int value;
    printf("Enter value to push: ");
    scanf("%d", &value);
    s->data[++(s->top)] = value;
    printf("Pushed %d\n", value);
}
void pop(Stack* s) {
    if (s->top == -1) {
        printf("Stack underflow!\n");
        return;
    }
    int value = s->data[(s->top)--];
    printf("Popped %d\n", value);
}
void display(Stack* s) {
    if (s->top == -1) {
        printf("Stack is empty.\n");
        return;
    }
    printf("Stack contents: ");
    for (int i = 0; i <= s->top; i++) {
        printf("%d ", s->data[i]);
    }
    printf("\n");
}
