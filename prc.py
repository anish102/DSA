a = [9,5,1,4,8,3,7]

def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

def selection_sort(a):
    n = len(a)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if a[j] < a[min_index]:
                min_index = j
        a[min_index] ,a[i] = a[i],a[min_index]
    return a

print(selection_sort(a))