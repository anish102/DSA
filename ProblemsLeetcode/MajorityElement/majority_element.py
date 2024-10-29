nums = [2, 3, 3, 4, 4, 4, 4, 4, 3]

count = 0
a = 0
for num in nums:
    if count == 0:
        a = num
    count += (1 if num == a else -1)

print(a)
