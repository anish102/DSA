def findDisappearedNumbers(nums):
    n = len(nums)
    result = []

    for num in nums:
        index = abs(num) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]
    print(nums)
    for i in range(n):
        if nums[i] > 0:
            result.append(i + 1)

    return result


print(findDisappearedNumbers([1, 1]))
