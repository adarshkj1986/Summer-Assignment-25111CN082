list=[1,2,3]
copied_list=list.copy()
copied_list.reverse()
if(copied_list==list):
    print("this is a palindrome")
else:
    print("not a palindrome")