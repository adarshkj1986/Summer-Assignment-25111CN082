

upper=1
lower=1001
print("armstrong between 1 and 1000 are:")
for n in range(upper,lower+1):
    temp=n
    count=0
    while temp>0:
        temp=temp//10
        count=count+1
    temp=n
    sum=0
    while temp>0:
        r=temp%10
        sum=sum+pow(r,count)
        temp=temp//10
    if sum==n:
       print(n)
 