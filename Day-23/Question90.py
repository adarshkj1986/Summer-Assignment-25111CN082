text="apple"
seen=[]
first_repeating=None
for char in text:
    if char in seen:
        first_repeating=char
        break
    else:
        seen.append(char)
if first_repeating:
    print("first repeating is:",first_repeating)
else:
    print("no repeating")