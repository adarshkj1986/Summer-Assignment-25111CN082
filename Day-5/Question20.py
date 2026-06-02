n=int(input("enter the number:"))
d=2
largest_prime=0
while(n>1):
    if (n%d==0):
        largest_prime=d
        n=n//d
    else:
        d+=1
print("largest prime factor is:",largest_prime)
    