# String Split and Join
# https://www.hackerrank.com/challenges/python-string-split-and-join/problem\


def split_and_join(line):
    # write your code here
    # a = "this is a string"
    a = line.split(" ") 
    a = "-".join(a)
    return a
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
