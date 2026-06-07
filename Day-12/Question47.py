def fibo(n):
    if (n<=0):
        print([])
        return
    elif n==1:
        print([0])
        return
    fib=[0,1]
    for i in range(2,n):
        next_term=fib[i-1]+fib[i-2]
        fib.append(next_term)
    print(fib)
fibo(5)