sentence="Hello everyone I am currently living in Delhi"
words=sentence.split()
longest_word=""
for word in words:
    if len(word)>len(longest_word):
        longest_word=word
print("the longest word is:",longest_word)
