
# Problem: Set .union() Operation
# HackerRank: https://www.hackerrank.com/challenges/py-set-union/problem

n = int(input())
english = set(map(int, input().split()))

b = int(input())
french = set(map(int, input().split()))

result = english.union(french)
print(len(result))
