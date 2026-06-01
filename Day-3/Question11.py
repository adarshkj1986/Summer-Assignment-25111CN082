a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
factor_a=set()
for i in range(1,a+1):
    if a%i==0:
        factor_a.add(i)
print()
factor_b=set()
for i in range(1,b+1):
    if b%i==0:
        factor_b.add(i)
common_factor=factor_a.intersection(factor_b)
print("the gcd is:",max(common_factor))

