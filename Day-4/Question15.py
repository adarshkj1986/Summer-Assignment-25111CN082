n=int(input("enter the number"))
count=0
n1=n
temp=n
while(temp>0):
    temp=temp//10
    count=count+1
sum=0

while(n>0):
    r=n%10
    sum=sum+pow(r,count)
    n=n//10
if(sum==n1):
    print("armstrong number")
else:
    print("not armstrong")
