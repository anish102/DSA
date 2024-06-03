word = "ffA"
state = False
count = 0

for i in word:
    if i.isupper():
        count += 1

if count == len(word) or count == 0 or (count == 1 and word[0].isupper()):
    state = True

print(state)

# if (
#     word == word.upper()
#     or word == word.lower()
#     or (word[0] == word[0].upper() and word[1:] == word[1:].lower())
# ):
#     print(True)
# print(False)
