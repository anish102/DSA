s="Hello"
s_list=list(s)
for i in range(len(s)):
    if ord(s[i]) >= 65 and ord(s[i])<=90:
      s_list[i] = chr(ord(s[i])+32)
s=''.join(s_list)
print(s)
