
# Problem: The Minion Game
# HackerRank: https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    kevin = 0
    stuart = 0
    length = len(string)
    
    for i in range(length):
        points = length - i
        
        if string[i] in "AEIOU":
            kevin += points
        else:
            stuart += points
            
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

  if __name__ == '__main__':
    s = input()
    minion_game(s)
