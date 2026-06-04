def rev_number(n,rev=0):              #n=123
    if(n==0):
        return rev
    else:
        return rev_number(n//10,(rev*10)+(n%10))     #n=123//10=22,rev=123%10=3        
print(rev_number(int(input("enter the number:"))))