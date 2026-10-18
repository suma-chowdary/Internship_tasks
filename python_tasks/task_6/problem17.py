
# Problem: Check Strict Superset
# HackerRank: https://www.hackerrank.com/challenges/py-check-strict-superset/problem

A = set(input().split())
n = int(input())

result = True

for _ in range(n):
    B = set(input().split())

    if not A > B:
        result = False
        break

print(result)
