# Collections.Counter()
# https://www.hackerrank.com/challenges/collections-counter/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

shoe_size = list(map(int,input().split()))
# print(n,shoe_size)
no_cust = int(input())

price = []
for i in range(no_cust):
    cust_shoe_s_Price = input().split()

    if int(cust_shoe_s_Price[0]) in shoe_size:
         price.append(int(cust_shoe_s_Price[1]))
         shoe_size.remove(int(cust_shoe_s_Price[0]))


print(sum(price))
