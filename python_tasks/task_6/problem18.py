
# Problem: Set Mutations
# HackerRank: https://www.hackerrank.com/challenges/py-set-mutations/problem

if __name__ == '__main__':
    n = int(input())
    a = set(map(int, input().split()))

    operations = int(input())

    for _ in range(operations):
        command = input().split()
        other_set = set(map(int, input().split()))

        if command[0] == 'update':
            a.update(other_set)
        elif command[0] == 'intersection_update':
            a.intersection_update(other_set)
        elif command[0] == 'difference_update':
            a.difference_update(other_set)
        elif command[0] == 'symmetric_difference_update':
            a.symmetric_difference_update(other_set)

    print(sum(a))
