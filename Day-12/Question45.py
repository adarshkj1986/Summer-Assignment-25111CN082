def palindrome(n): # thsi is palindrome because reading from first this is 1,2,1 and from last it is also 1,2,1
    copied=n.copy()
    copied.reverse()
    if(n==copied):
        print("this is palindrome")
    else:
        print("this is not palindrome")
palindrome([1,2,1])

