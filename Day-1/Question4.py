n=int(input("enter the number:"))
count=0
if n==0:
    count=1
while n>0:
    count+=1
    n=n//10
print("total digits:",count)