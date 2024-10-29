nums = [1, 3, 1]

# print(2*sum(set(nums))-sum(nums))
result = 0
for num in nums:
    result ^= num

print(result)
