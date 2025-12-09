#include<stdio.h>
int main()
{
int i,arr[10];
printf("enter 10 elements: \n");
for(i=0;i<10;i++)
{
scanf("%d",&arr[i]);
}
printf("array element are : \n");
for(i=0;i<10;i++)
{
printf("%d\n",arr[i]);
}
return 0;
}
