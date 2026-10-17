

# Problem: Piling Up!
# HackerRank: https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    cubes = deque(map(int, input().split()))
    last = float('inf')
    possible = True

    while cubes:
        if cubes[0] >= cubes[-1]:
            chosen = cubes.popleft()
        else:
            chosen = cubes.pop()

        if chosen > last:
            possible = False
            break

        last = chosen

    if possible:
        print("Yes")
    else:
        print("No")
