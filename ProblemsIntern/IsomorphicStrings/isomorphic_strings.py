s = "badc"
t = "baba"

############### My approach###########
# pair = {}
# res = []
# s1 = list(s)
# t1 = list(t)
# if (len(set(s1)) == len(set(t1))):
#     for i in range(len(s1)):
#         pair[s1[i]] = t1[i]
#     for i in range(len(s1)):
#         res.append(pair[s1[i]])
#     final = "".join(res)
#     print(pair)
#     print(final)
#     if final == t:
#         print(True)
#     else:
#         print(False)
# else:
#     print(False)

a = len(set(zip(s, t)))
b = len(set(s))
c = len(set(t))
print(a)
print(b)
print(c)
