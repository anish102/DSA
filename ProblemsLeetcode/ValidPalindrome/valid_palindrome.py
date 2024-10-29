s = "A man, a plan, a canal: Panama"

res = (''.join(char for char in s if char.isalnum())).lower()
rev = res[::-1]
if (res == rev):
    print(True)
else:
    print(False)
