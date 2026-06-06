def prime(n):
    if n<=1:
        print("not a prime number")
        return
    for i in range(2,n):
        if n%i==0:
            print("not a prime number")
            return
    print("prime number")
prime(5)