n=int(input("enter the number:"))
factor_n=set()
for i in range(1,n+1):
    if(n%i==0):
       factor_n.add(i)
print("the factors of this numbers are:",factor_n)

