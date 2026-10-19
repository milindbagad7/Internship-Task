# 10. Sawp Case
# https://www.hackerrank.com/challenges/swap-case/problem
def swap_case(s):
    swap = ''
    for i in s:
        if i.islower():
            swap =swap+i.upper()
        elif i.isupper():
            swap = swap + i.lower()
        else:
            swap = swap + i
    return swap

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
