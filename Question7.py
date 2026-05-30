n=int(input("enter the number:"))
pro=1
while (n>0):
    r=n%10
    pro*=r
    n=n//10
print("product is:",pro)