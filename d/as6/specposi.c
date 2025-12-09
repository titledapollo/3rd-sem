#include <stdio.h>

#define MAX 100

struct Node {
    int data;
    int next;
};

struct Node nodes[MAX];
int head = -1;
int freeIndex = 0;

int createNode(int data) {
    if (freeIndex >= MAX) {
        printf("No more space to create node!\n");
        return -1;
    }
    int newIndex = freeIndex++;
    nodes[newIndex].data = data;
    nodes[newIndex].next = -1;
    return newIndex;
}

void insertAtBeginning(int data) {
    int newNode = createNode(data);
    if (newNode == -1) return;
    nodes[newNode].next = head;
    head = newNode;
}

void insertAtEnd(int data) {
    int newNode = createNode(data);
    if (newNode == -1) return;
    if (head == -1) {
        head = newNode;
    } else {
        int temp = head;
        while (nodes[temp].next != -1) {
            temp = nodes[temp].next;
        }
        nodes[temp].next = newNode;
    }
}

void insertAfterPosition(int data, int position) {
    int temp = head;
    for (int i = 1; i < position && temp != -1; i++) {
        temp = nodes[temp].next;
    }
    if (temp == -1) {
        printf("Position out of range!\n");
        return;
    }
    int newNode = createNode(data);
    if (newNode == -1) return;
    nodes[newNode].next = nodes[temp].next;
    nodes[temp].next = newNode;
}

void displayList() {
    if (head == -1) {
        printf("List is empty!\n");
        return;
    }
    int temp = head;
    while (temp != -1) {
        printf("%d -> ", nodes[temp].data);
        temp = nodes[temp].next;
    }
    printf("NULL\n");
}

int main() {
    int choice, data, pos;
    while (1) {
        printf("\n--- Linked List Menu ---\n");
        printf("1. Insert at Beginning\n");
        printf("2. Insert at End\n");
        printf("3. Insert After Position\n");
        printf("4. Display List\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter data: ");
                scanf("%d", &data);
                insertAtBeginning(data);
                break;
            case 2:
                printf("Enter data: ");
                scanf("%d", &data);
                insertAtEnd(data);
                break;
            case 3:
                printf("Enter data: ");
                scanf("%d", &data);
                printf("Enter position: ");
                scanf("%d", &pos);
                insertAfterPosition(data, pos);
                break;
            case 4:
                displayList();
                break;
            case 5:
                return 0;
            default:
                printf("Invalid choice! Try again.\n");
        }
    }
}