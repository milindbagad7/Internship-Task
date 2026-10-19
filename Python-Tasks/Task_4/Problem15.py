# 15.Word Order
# https://www.hackerrank.com/challenges/word-order/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
word = set()
count = 0
dic = {}
for i in range(n):
    a = input()
    word.add(a)
    if a not in dic:
        dic[a] = 1
    else:
        dic[a] +=1

print(len(word))
for v in dic.values():
    print(v,end =" ")
