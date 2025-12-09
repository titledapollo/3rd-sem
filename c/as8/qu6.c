#include <stdio.h>

struct Employee {
    char name[50];
    int id;
    float salary;
};

int main() {
    struct Employee emp[100];
    int n, i;
    float limit;

    printf("Enter number of employees: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        printf("\n--- Enter details of Employee %d ---\n", i + 1);
        printf("Enter name: ");
        scanf(" %[^\n]", emp[i].name);

        printf("Enter ID: ");
        scanf("%d", &emp[i].id);

        printf("Enter salary: ");
        scanf("%f", &emp[i].salary);
    }

    printf("\nEnter the salary limit: ");
    scanf("%f", &limit);

    printf("\n--- Employees with Salary Above %.2f ---\n", limit);
    int found = 0;
    for (i = 0; i < n; i++) {
        if (emp[i].salary > limit) {
            found = 1;
            printf("\nName   : %s", emp[i].name);
            printf("\nID     : %d", emp[i].id);
            printf("\nSalary : %.2f\n", emp[i].salary);
        }
    }

    if (!found) {
        printf("\nNo employee has salary above %.2f\n", limit);
    }

    return 0;
}

