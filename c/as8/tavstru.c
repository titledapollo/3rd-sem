#include <stdio.h>

struct Student {
    char name[50];
    int rollNumber;
    float marks[3];
    float total;
    float average;
};

int main() {
    struct Student s[5];
    int i, j;

    printf("Enter details of 5 students:\n");

    for (i = 0; i < 5; i++) {
        printf("\n--- Student %d ---\n", i + 1);
        printf("Enter name: ");
        scanf(" %[^\n]", s[i].name);

        printf("Enter roll number: ");
        scanf("%d", &s[i].rollNumber);

        s[i].total = 0;
        printf("Enter marks in 3 subjects:\n");
        for (j = 0; j < 3; j++) {
            printf("Subject %d: ", j + 1);
            scanf("%f", &s[i].marks[j]);
            s[i].total += s[i].marks[j];
        }

        s[i].average = s[i].total / 3.0;
    }

    printf("\n\n--- Student Results ---\n");
    for (i = 0; i < 5; i++) {
        printf("\nName: %s", s[i].name);
        printf("\nRoll Number: %d", s[i].rollNumber);
        printf("\nTotal Marks: %.2f", s[i].total);
        printf("\nAverage Marks: %.2f\n", s[i].average);
    }

    return 0;
}

