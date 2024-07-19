def sumOfTheDigitsOfHarshadNumber(x):
    temp = [int(i) for i in str(x)]
    dvder = sum(temp)
    if (x % dvder == 0):
        return dvder
    return -1
