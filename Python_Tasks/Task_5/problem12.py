
# Problem: Capitalize!
# HackerRank: https://www.hackerrank.com/challenges/capitalize/problem

def solve(s):
    words = s.split(' ')
    result = []
    for word in words:
        result.append(word.capitalize())
    return ' '.join(result)

if __name__ == '__main__':
    s = input()
    print(solve(s))
