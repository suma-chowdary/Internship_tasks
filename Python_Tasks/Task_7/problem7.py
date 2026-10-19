
# Problem: Alphabet Rangoli
# Link: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    lines = []

    for i in range(size):
        s = "-".join(alphabet[size-1:i:-1] + alphabet[i:size])
        lines.append(s.center(4 * size - 3, "-"))

    print("\n".join(lines[:0:-1] + lines))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
