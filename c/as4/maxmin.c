#include <stdio.h>
int main ()
{
int n, i, max ,min ;
	printf("Enter the size of an array: ");
	scanf("%d", &n);
	int arr[n];
	printf("Enter %d elements:\n",n);
	for(i = 0; i < n; i++){
	scanf("%d",&arr[i]);
	}
	
	max=min=arr[0];
	for(i=1;i<n;i++){
		if (arr[i]>max)max=arr[i];
		if (arr[i]<min)min=arr[i];
		}
	printf("Maximum number are: %d\n",max);
	printf("Minimum number are: %d\n",min);
	return 0;
	}
