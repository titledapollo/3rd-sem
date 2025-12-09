#include <stdio.h>
int main ()
{
int n, i,sum;
	printf("Enter the size of an array: ");
	scanf("%d", &n);
	int arr[n];
	printf("Enter %d elements:\n",n);
	for(i = 0; i < n; i++){
	scanf("%d",&arr[i]);
	sum+=arr[i];
	
	}
	printf("Sum of all elements are: %d\n",sum);
	return 0;
}
