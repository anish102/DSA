n = 8

if n == 1:
    print(1)
else:
    low = 1
    high = n
    while low <= high:
        mid = (low + high) // 2
        sum = (mid * (mid + 1) // 2)
        if sum == n:
            print(mid)
            break
        elif sum > n:
            if sum - mid < n:
                print(mid - 1)
                break
            high = mid - 1
        else:
            low = mid + 1
