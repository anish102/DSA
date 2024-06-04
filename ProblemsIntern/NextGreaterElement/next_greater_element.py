nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

ans = []
for i in nums1:
    for j in range(nums2.index(i), len(nums2)):
        if nums2[j] > i:
            ans.append(nums2[j])
            break
        elif(j == len(nums2) - 1):
            ans.append(-1)
            break
print(ans)
