
# Problem: Set .symmetric_difference() Operation
# Link: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

if __name__ == '__main__':
    n = int(input())
    english = set(map(int, input().split()))

    m = int(input())
    french = set(map(int, input().split()))

    result = english.symmetric_difference(french)
    print(len(result))
