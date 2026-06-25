a=input("enter the string:")
text=a.lower()
if(text==text[::-1]):       #to check if the string from first and last is same or not
    print("palindrome")
else:
    print("not palindrome")