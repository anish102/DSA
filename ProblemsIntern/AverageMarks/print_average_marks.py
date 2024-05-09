if __name__ == '__main__':
    student_marks = {'a': [20, 30, 47],
                     'b': [50, 60, 10],
                     'c': [40, 45, 50]}
    res = 0
    query = input("enter name")
    # for key, value in student_marks.items():
    #     if key == query:
    #         res = sum(value)/len(value)
    # print(res)

    res = [sum(value)/len(value)
           for key, value in student_marks.items() if query == key]
    print(res[0])
