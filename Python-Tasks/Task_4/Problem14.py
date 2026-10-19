# Set .add()
# https://www.hackerrank.com/challenges/py-set-add/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

country = set()
count = 0

for i in range(n):
    country.add(input())

for j in country:
    count +=1
print(count)

