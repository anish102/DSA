# Given two arrays of strings list1 and list2, find the common strings with the least index sum.


def findCommon(a, b):
    pair = {}
    for i in a:
        if i in b:
            pair[i] = a.index(i) + b.index(i)
    return [key for key in pair if pair[key]==min(pair.values())]


print(
    findCommon(
        ["Shogun", "Tapioca Express", "Burger King", "KFC"],
        [
            "Piatti",
            "The Grill at Torrey Pines",
            "Hungry Hunter Steakhouse",
            "Shogun",
            "KFC",
        ],
    )
)
