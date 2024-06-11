def isPowerofTwo(n):
    if n == 2 or n == 1:
        return True
    elif n < 2 and n != 1:
        return False
    return isPowerofTwo(n / 2)


n = 5454
print(n>0 and (n & (n-1) == 0))