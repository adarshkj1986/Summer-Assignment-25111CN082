#include<stdio.h>
int main(){
    int n,i;
    printf("enter the number:");
    scanf("%d",&n);
    int fact=1;
    i=1;
    while(i<=n){
        fact=fact*i;
        i++;
    }
   
    printf(" fact %d is %d\n",n,fact);
    return 0;

}