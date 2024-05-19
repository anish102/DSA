s = "ab"
t = "bya"

s1 = list(s)
t1 = list(t)
s1.sort()
t1.sort()
if s != "":
    for i in range(len(s1)):
        if (s1[i] != t1[i]):
            print(t1[i])
            break
        elif (i == len(s1)-1):
            print(t1[i+1])
            break
else:
    print(t)
