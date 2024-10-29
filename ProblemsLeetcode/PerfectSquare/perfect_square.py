num = 133225

state = False
if (num == 1 or num == 0):
    state = True
else:
    low = 1
    high = num
    while (low <= high):
        mid = (low+high)//2
        if mid*mid == num:
            state = True
            break
        elif mid*mid > num:
            high = mid-1
        else:
            low = mid+1
print(state)
