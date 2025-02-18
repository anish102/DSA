# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard.


def find_words(words):
    row1 = list("qwertyuiop")
    row2 = list("asdfghjkl")
    row3 = list("zxcvbnm")
    result = []
    for word in words:
        word_lower = word.lower()
        if all(char in row1 for char in word_lower):
            result.append(word)
        elif all(char in row2 for char in word_lower):
            result.append(word)
        elif all(char in row3 for char in word_lower):
            result.append(word)
    return result


print(find_words(["Hello", "Alaska", "Dad", "Peace"]))
