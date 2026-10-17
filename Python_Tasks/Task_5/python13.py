
# Problem: Nested Lists
# HackerRank: https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    grades = sorted(set(student[1] for student in students))
    second_lowest = grades[1]
    names = []

    for student in students:
        if student[1] == second_lowest:
            names.append(student[0])

    for name in sorted(names):
        print(name)
