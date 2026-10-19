
# Problem: Separate the Numbers
# Link: https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separateNumbers(s):
    for i in range(1, len(s) // 2 + 1):
        first = s[:i]

        if first[0] == '0':
            continue

        current = int(first)
        result = first

        while len(result) < len(s):
            current += 1
            result += str(current)

        if result == s:
            print("YES", first)
            return

    print("NO")


if __name__ == '__main__':
    q = int(input().strip())

    for _ in range(q):
        s = input().strip()
        separateNumbers(s)
