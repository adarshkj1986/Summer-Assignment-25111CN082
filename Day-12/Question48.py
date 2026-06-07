def perfect(n):                        # if n is 6 
    factor_sum=0                       # perfect number is when factors sum is equals to the original number
    for i in range(1,n):               # range will be 1,2,3,4,5
        if(n%i==0):                    # n%i==0 is when i is 1,2,3 
          factor_sum+=i
    if(factor_sum==n):
       print("this is a perfect number")
    else:
       print("this is not a perfect number")
perfect(6)


