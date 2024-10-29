def isUgly(n):
    if n <= 0:
        return False
    for prime in [2, 3, 5]:
        while n % prime == 0:
            n //= prime
    return n == 1
