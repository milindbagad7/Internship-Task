# 18. The Minion Game
# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
def minion_game(string):
    vowels = "AEIOU"
    Kevin = 0
    Stuart = 0
    for i in range(len(string)):
        points = len(string)- i
        if string[i] in vowels:
            Kevin += points
        else:
            Stuart +=points
    if Stuart > Kevin:
        print("Stuart",Stuart)
    elif Stuart == Kevin:
        print("Draw")
    else:
        print("Kevin",Kevin)
if __name__ == '__main__':
    s = input()
    minion_game(s)
