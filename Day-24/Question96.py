text="programming"
result=""
for char in text:
    if char not in result:
        result+=char
print("origianl:",text)
print("after removing duplicate characters:",result)