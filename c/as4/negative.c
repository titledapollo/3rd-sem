#include <stdio.h>
int main ()
{
 int arr[100],i , n;
 printf("Enter the size of array : ");
 scanf("%d",&n);
  for (i = 0 ; i < n ; i ++)
  	{
  	  printf("Enter the  element of array : ");
  	  scanf("%d",&arr[i]);	  
  	}
 printf("\ngiven array is  : ");
 for (i = 0 ; i < n ; i ++)
 {
 printf("%d\t\t",arr[i]);
 }
 printf("\n negative number is  : ");
 for (i = 0 ; i < n ; i ++)
 {
 	if (arr[i]< 0 )
 	{
 		printf("%d\t",arr[i]);
 	}
 }
printf("\n");
return 0;
}
