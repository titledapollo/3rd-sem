#include<stdio.h>
int main()
{
  float p,t,r,si;
  printf("enter principle , time , rate :  ");
  scanf("%f%f%f",&p,&t,&r);
  si=p*t*r/100;
  printf("simple interest is : %f\n",si);
  return 0;
}
