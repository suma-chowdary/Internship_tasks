
# Problem: Gemstones
# Link: https://www.hackerrank.com/challenges/gem-stones/problem

def gemstones(arr):
    common = set(arr[0])

    for rock in arr[1:]:
        common = common.intersection(set(rock))

    return len(common)


if __name__ == '__main__':
    n = int(input().strip())
    arr = []

    for _ in range(n):
        arr.append(input().strip())

    print(gemstones(arr))
