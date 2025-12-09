#include <stdio.h>

struct Employee {
    char name[50];
    int id;
    float salary;
};

void inputEmployee(struct Employee *e) {
    printf("Enter employee name: ");
    scanf(" %[^\n]", e->name);

    printf("Enter employee ID: ");
    scanf("%d", &e->id);

    printf("Enter employee salary: ");
    scanf("%f", &e->salary);
}

void displayEmployee(struct Employee e) {
    printf("\n--- Employee Details ---\n");
    printf("Name   : %s\n", e.name);
    printf("ID     : %d\n", e.id);
    printf("Salary : %.2f\n", e.salary);
}

int main() {
    struct Employee emp;

    inputEmployee(&emp);
    displayEmployee(emp);

    return 0;
}

