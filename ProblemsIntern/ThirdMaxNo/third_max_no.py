nums = [2, 2, 3, 1]

a = list(set(nums))
a.sort(reverse=True)
if len(a) <= 2:
    print(a[0])
else:
    print(a[2])
