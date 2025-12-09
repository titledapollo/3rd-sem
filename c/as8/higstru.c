#include <stdio.h>

struct Student {
    char name[50];
    int rollNumber;
    float marks;
};

int main() {
    struct Student s[5];
    int i, topIndex = 0;

    printf("Enter details of 5 students:\n");
    for (i = 0; i < 5; i++) {
        printf("\n--- Student %d ---\n", i + 1);
        printf("Enter name: ");
        scanf(" %[^\n]", s[i].name);

        printf("Enter roll number: ");
        scanf("%d", &s[i].rollNumber);

        printf("Enter marks: ");
        scanf("%f", &s[i].marks);
    }

    for (i = 1; i < 5; i++) {
        if (s[i].marks > s[topIndex].marks) {
            topIndex = i;
        }
    }

    printf("\n--- Student with Highest Marks ---\n");
    printf("Name: %s\n", s[topIndex].name);
    printf("Roll Number: %d\n", s[topIndex].rollNumber);
    printf("Marks: %.2f\n", s[topIndex].marks);

    return 0;
}

