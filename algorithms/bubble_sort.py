def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        print(i)
        for j in range(n - i):
            a = arr[j]
            if a != arr[-1]:
                b = arr[j+1]
                if a > b:
                    arr[j] = b
                    arr[j+1] = a
    return arr


print(bubbleSort([5, 3, 8, 1, 9, 4, 6]))
