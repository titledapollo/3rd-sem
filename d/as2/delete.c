#include<stdio.h>
int main()
{
   int arr[100],n,i,pos,choice;
   printf("Enter the number of an elements:");
   scanf("%d",&n);
   printf("Enter %d elements:\n",n);
   for(i=0; i<n; i++)
   {
      scanf("%d",&arr[i]);
   }
   printf("Choose deletion option:\n");
   printf(" 1. From Beginning\n 2. From End\n 3. From any position\n");
   scanf("%d",&choice);
   
   if(n == 0){
       printf("Array is empty Nothin to delete:\n");
       return 0;
   }  
   if(choice == 1) 
   { 
      for(i=0; i<n-1; i++){
          arr[i] = arr[i+1];
          }
          n--;
   }
   else if(choice == 2){
          n--;
      }
      
   else if(choice == 3){
       printf("Enter position to delete (1 to %d): ",n);
       scanf("%d",&pos);
       if(pos<1 || pos>n){
          printf("Invalid position!\n"); }
           else{
              for(i=pos; i<n-1; i++){
                 arr[i] = arr[i+1];
              }
              n--;}
              }
    else{
       printf("Invalid choice!\n");
       }
     printf("Array after deletion:\n");
     for(i=0; i<n; i++) {
         printf(" %d\n" ,arr[i]);
       }
       return 0;                
 }           
