str1="ABCDE"
str2="EDCBA"
if len(str1)==len(str2) and str2 in(str1+str2):
    print("yes rotation")
else:
    print("no rotation")