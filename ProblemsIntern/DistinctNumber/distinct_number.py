nums = [1, 2, 4, 3, 7, 1]

# nums.sort()
# state = False
# for i in range(len(nums)):
#     if i != len(nums)-1:
#         if nums[i] == nums[i+1]:
#             state = True
#             break
# print(state)

s = set(nums)
if (len(s) == len(nums)):
    print(False)
else:
    print(True)
