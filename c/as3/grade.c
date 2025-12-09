#include <stdio.h>

char getGrade(int marks) {
    if (marks >= 90 && marks <= 100)
        return 'A';
    else if (marks >= 75 && marks <= 89)
        return 'B';
    else if (marks >= 60 && marks <= 74)
        return 'C';
    else if (marks >= 40 && marks <= 59)
        return 'D';
    else if (marks >= 0 && marks < 40)
        return 'F';
    else
        return 'I'; // Invalid marks
}

int main() {
    int marks[5];
    char *subjects[5] = {"Chemistry", "Physics", "Mathematics", "English", "Biology"};
    char grade;
    int i;

    for (i = 0; i < 5; i++) {
        printf("Enter %s marks (out of 100): ", subjects[i]);
        scanf("%d", &marks[i]);
    }

    printf("\nGrades:\n");
    for (i = 0; i < 5; i++) {
        grade = getGrade(marks[i]);
        if (grade == 'I') {
            printf("%s: Invalid marks entered.\n", subjects[i]);
        } else {
            printf("%s: %c\n", subjects[i], grade);
        }
    }

    return 0;
}

