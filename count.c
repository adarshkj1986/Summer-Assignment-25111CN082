#include<stdio.h>
int main(){
    int n,i,count=0;
    printf("enter the number:");
    scanf("%d",&n);
    i=1;
    if(n==0){
        count=1;
    }
    else{

        while(i<=n){
        n=n/10;
        count++;
        i++;
    }
}
    printf(" total digits is %d is %d\n",n,count);
    return 0;
}