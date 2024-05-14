nums = [0, 1]

# Brute force approach
# nums.sort()
# a = len(nums)
# print(a)
# for i in range(a+1):
#     if nums[a-1] == a:
#         if i != nums[i]:
#             print(i)
#             break
#     else:
#         print(a)
#         break

# Sum approack
a = sum(nums)
b = len(nums)*(len(nums)+1)/2
print(int(b-a))
