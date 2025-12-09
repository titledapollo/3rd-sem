#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

void printList(struct Node* head) {
    while (head != NULL) {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

struct Node* insertAtEnd(struct Node* head, int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = NULL;
    if (head == NULL) return newNode;
    struct Node* t = head;
    while (t->next != NULL) t = t->next;
    t->next = newNode;
    return head;
}

struct Node* deleteAtPosition(struct Node* head, int pos) {
    if (pos == 1) {
        struct Node* t = head;
        head = head->next;
        free(t);
        return head;
    }
    struct Node* t = head;
    for (int i = 1; i < pos - 1 && t != NULL; i++) t = t->next;
    if (t == NULL || t->next == NULL) return head;
    t->next = t->next->next;
    return head;
}

int main() {
    struct Node* head = NULL;
    head = insertAtEnd(head, 10);
    head = insertAtEnd(head, 20);
    head = insertAtEnd(head, 30);
    head = insertAtEnd(head, 40);
    head = insertAtEnd(head, 50);

    printf("Original list:\n");
    printList(head);

    int pos;
    printf("Enter position to delete: ");
    scanf("%d", &pos);

    head = deleteAtPosition(head, pos);
    printf("After deleting at position %d:\n", pos);
    printList(head);

    return 0;
}

