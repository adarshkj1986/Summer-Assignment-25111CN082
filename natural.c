#include<stdio.h>
int main(){
    int n,i;
    int sum=0;
    printf("enter the number:");
    scanf("%d",&n);
    for(i=1;i<=n;i++){
        sum+=i;

    }
    printf("the sum is %d is %d\n",n,sum);
    return 0;

}