str1="apple"
str2="mango"
common=""
for char in str1:
    if char in str2 and char not in common:
        common+=char
print("common characters are:",common)