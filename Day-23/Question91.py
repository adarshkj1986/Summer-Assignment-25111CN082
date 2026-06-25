str1="listen"
str2="silent"
s1=str1.replace(" ","").lower()
s2=str2.replace(" ","").lower()
if len(s1)!=len(s2):
    print("not anagram")
else:
    if sorted(s1)==sorted(s2):
        print("these are anagrams")
    else:
        print("not anagrams")