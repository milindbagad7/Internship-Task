# 12.Introduction to Sets
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
def average(array):
    # your code goes here
    s = set(array)
    suma = sum(s)
    le = len(s)
    average = suma/le
    return average
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
