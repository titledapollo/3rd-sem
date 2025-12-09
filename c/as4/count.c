#include <stdio.h>
int main ()
{
 int arr[100],i , n,evencount=0,oddcount=0;
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
 printf("%d\t",arr[i]);
 }
 for (i = 0 ; i < n  ; i ++)
 {
 	if (arr[i]%2==0){
 	evencount++;
 	}
 	else{
 	oddcount++;
 	}
 }
 printf("even  number is : %d\n",evencount);
 printf("odd  number is : %d\n",oddcount);
 }
