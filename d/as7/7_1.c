#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

void printList(struct Node* head) {
    struct Node* temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}

struct Node* insertAtEnd(struct Node* head, int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = NULL;
    if (head == NULL) return newNode;
    struct Node* temp = head;
    while (temp->next != NULL) temp = temp->next;
    temp->next = newNode;
    return head;
}

struct Node* deleteAtBeginning(struct Node* head) {
    if (head == NULL) return NULL;
    struct Node* temp = head;
    head = head->next;
    free(temp);
    return head;
}

struct Node* deleteAtEnd(struct Node* head) {
    if (head == NULL) return NULL;
    if (head->next == NULL) {
        free(head);
        return NULL;
    }
    struct Node* temp = head;
    while (temp->next->next != NULL) temp = temp->next;
    free(temp->next);
    temp->next = NULL;
    return head;
}

struct Node* deleteAfterPosition(struct Node* head, int position) {
    struct Node* temp = head;
    for (int i = 1; i < position && temp != NULL; i++) temp = temp->next;
    if (temp == NULL || temp->next == NULL) return head;
    struct Node* del = temp->next;
    temp->next = del->next;
    free(del);
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

    head = deleteAtBeginning(head);
    printf("After deleting at beginning:\n");
    printList(head);

    head = deleteAtEnd(head);
    printf("After deleting at end:\n");
    printList(head);

    head = deleteAfterPosition(head, 2);
    printf("After deleting after position 2:\n");
    printList(head);

    return 0;
}

