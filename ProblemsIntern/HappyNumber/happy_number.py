def isHappy(n):
    res = n
    while res > 9:
        if res == 1 or res == 7:
            return True
        temp = [int(i) ** 2 for i in str(res)]
        res = sum(temp)
    if res == 1 or res == 7:
        return True
    return False


print(isHappy(7))
