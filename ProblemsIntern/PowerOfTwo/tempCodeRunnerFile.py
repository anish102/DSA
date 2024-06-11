    if n == 2 or n == 1:
        return True
    elif n < 2 and n != 1:
        return False
    return isPowerofTwo(n / 2)