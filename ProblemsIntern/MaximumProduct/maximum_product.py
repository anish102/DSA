def maximumProduct(nums):
  nums.sort()
  n = len(nums)
  max_product = nums[-1] * nums[-2] * nums[-3]
  min_product = nums[0] * nums[1] * nums[-1]
  return max(max_product, min_product)
