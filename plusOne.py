"""You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits."""


def plusOne(digits):
    res = 0
    for i in digits:
        res = res * 10 + i
    res = res + 1
    temp = str(res)
    fnl = []
    for j in temp:
        fnl.append(int(j))
    return fnl


print(plusOne([1, 2, 9]))
