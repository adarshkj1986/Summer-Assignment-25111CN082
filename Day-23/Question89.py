text="hello"
result=None
for i in range(len(text)):
    is_repeated=False
    for j in range(len(text)):
        if i!=j and text[i]==text[j]:
            is_repeated=True
            break
    if not is_repeated:
        result=text[i]
        break
if result:
    print("the first non-repeating is:",result)
else:
    print("no repeating found")