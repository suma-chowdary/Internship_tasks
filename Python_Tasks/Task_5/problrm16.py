
# Problem: collections.Counter()
# HackerRank: https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

n = int(input())
shoe_sizes = Counter(map(int, input().split()))

customers = int(input())
total_money = 0

for _ in range(customers):
    size, price = map(int, input().split())

    if shoe_sizes[size] > 0:
        total_money += price
        shoe_sizes[size] -= 1

print(total_money)
