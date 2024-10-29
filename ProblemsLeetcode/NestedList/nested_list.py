if __name__ == '__main__':
    record = []
    for _ in range(int(input("Enter a number of students:"))):
        name = input("Enter a name:")
        score = float(input("Enter a score:"))
        record.append([name, score])
    unset_marks = [val for key, val in dict(record).items()]
    set_marks = list(set(unset_marks))
    set_marks.sort()
    print(set_marks)
    low_marks = set_marks[1]
    stud = [key for key, val in dict(record).items() if val == low_marks]
    stud.sort()
    for i in stud:
        print(i)
