num = 564564654

# My approach
# lst = [i for i in range(1, num) if num % i == 0]
# res = sum(lst)
# if res == num:
#     print(True)
# else:
#     print(False)


if num == 1:
    print(False)
count = 1
for i in range(2, int(num**0.5)+1):
    if num % i == 0:
        count += i+num//i
print(num == count)
