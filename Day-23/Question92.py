text="programming"
max_char=""
max_count=0
for char in text:
    count=text.count(char)
    if count>max_count:
        max_count=count
        max_char=char
print("the maximum occuring character is:",max_char)
print("it appears",max_count,"times")