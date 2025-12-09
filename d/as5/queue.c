#include <stdio.h>
#define SIZE 5

int queue[SIZE];
int front = -1, rear = -1;

void enqueue(int value) {
    if (rear == SIZE - 1) {
        printf("Queue is Full!\n");
    } else {
        if (front == -1)
            front = 0;
        rear++;
        queue[rear] = value;
        printf("%d enqueued to the queue.\n", value);
    }
}

void dequeue() {
    if (front == -1 || front > rear) {
        printf("Queue is Empty!\n");
    } else {
        printf("%d dequeued from the queue.\n", queue[front]);
        front++;
    }
}

void display() {
    if (front == -1 || front > rear) {
        printf("Queue is Empty!\n");
    } else {
        printf("Queue elements: ");
        for (int i = front; i <= rear; i++) {
            printf("%d ", queue[i]);
        }
        printf("\n");
    }
}

int main()
	{
	 int value ,choice ;
     while(1){
   		printf("\n\tQUEUE MENU \n");
   		printf("1.QUEUE (INSERTING):\n ");
   		printf("2.DEQUEUE(DELETING):\n  ");
   		printf("3.DISPLAY:\n ");
   		printf("4.EXIT:\n ");
   		printf("ENTER YOUR CHOICE  : ");
   		scanf("%d",&choice);
   		
   		if(choice == 1)
   		{
   			printf("ENTER THE VALUE : ");
   			scanf("%d",&value);
   			enqueue(value);
   		}
   		else if(choice == 2)
   		{
   			dequeue();
   		}
   		else if (choice == 3)
   		{
   			display();
   		}
   		else if(choice == 4)
   		{
   			printf("==PROGRAM ENDED==");
   			break ;
   		}
   		else 
   		{
   			printf("INVALID CHOICE \n");
   		}
   }

    return 0;
}

