string="Hello World"
vowels="aeiouAEIOU"
vowel_count=0
consonant_count=0
for char in string:
    if char.isalpha():
        if char in vowels:
            vowel_count+=1
        else:
            consonant_count+=1
print("vowels are:",vowel_count)
print("consonant are:",consonant_count)
