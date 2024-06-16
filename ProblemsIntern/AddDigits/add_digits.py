num = 81

a = num

while len(list(str(a))) != 1:
    x =[int(i) for i in list(str(a))]
    a = sum(x)
print(a)

# result = (num - 1) % 9 +1
