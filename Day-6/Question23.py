n=int(input("enter the number"),2)
count=0
while(n>0):
    if n%2==1:
        count=count+1
    n=n//2
print("set bits are:",count)