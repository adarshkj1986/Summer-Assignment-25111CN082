n=int(input("enter the end point till you want the multiple:"))
a=int(input("enter the first number:"))
b=int(input("enter the second number"))
multi_a=set()
for i in range(1,n):
    multi_a.add(a*i)
print()
multi_b=set()
for i in range(1,n):
    multi_b.add(b*i)
common_multi=multi_a.intersection(multi_b)
print("the lcm of two numbers are:",min(common_multi))