# flowerbed = [1]
# n = 1

# count = 0
# for i in range(len(flowerbed)):
#     if (len(flowerbed) != 1):
#         if (i == 0):
#             if (flowerbed[i] == 0 and flowerbed[i+1] == 0):
#                 flowerbed[i] = 1
#                 count += 1
#         elif (i == len(flowerbed)-1):
#             if (flowerbed[i] == 0 and flowerbed[i-1] == 0):
#                 flowerbed[i] = 1
#                 count += 1
#         else:
#             if (flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
#                 flowerbed[i] = 1
#                 count += 1
#     else:
#         if i == 0:
#             flowerbed[i] = 1
#             count += 1
#             break

# print(count)

# if n <= count:
#     print(True)
# else:
#     print(False)

flowerbed = [1]
n = 1

count = 0
length = len(flowerbed)
for i in range(length):
    if length == 1:
        if flowerbed[0] == 0:
            count += 1
        break
    if i == 0:
        if flowerbed[i] == 0 and flowerbed[i + 1] == 0:
            flowerbed[i] = 1
            count += 1
    elif i == length - 1:
        if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
            flowerbed[i] = 1
            count += 1
    else:
        if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
            flowerbed[i] = 1
            count += 1

print(count)

if n <= count:
    print(True)
else:
    print(False)
