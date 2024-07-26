def fizzBuzz(n):
    res = [
        (
            "FizzBuzz"
            if i % 5 == 0 and i % 3 == 0
            else "Buzz" if i % 5 == 0 else "Fizz" if i % 3 == 0 else str(i)
        )
        for i in range(1, n + 1)
    ]
    return res


print(fizzBuzz(15))
