# Symmetric Difference
# https://www.hackerrank.com/challenges/symmetric-difference/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
    
if __name__ == '__main__':
    m = int(input())
    a = set(map(int,input().split()))
    n = int(input())
    b = set(map(int,input().split()))

    result = sorted(a.symmetric_difference(b))
    for i in result:
        print(i)
