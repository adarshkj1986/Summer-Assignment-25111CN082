#include<stdio.h>
int main(){
    int n,n1,rev=0,r,count=0;
    printf("enter the number");
    scanf("%d",&n);
    n1=n;
    while(n>0){
        n=n/10;
        count++;
    }
    n=n1;
    while(n>0){
        r=n%10;
        rev=rev*10+r;
        n=n/10;
    }
    if(rev==n1){
        printf("this is a palindrome");
    }
    else{
        printf("not a palindrome");
    }
    return 0;
}