# Merge the Tools!
# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
def merge_the_tools(string, k):    # AAA BCA DDE
    # your code goes here
    for i in range(0,len(string),k):
        substring = string[i:i+k]
        uniquie = ""
        for j in substring:
            if j not in uniquie:
                uniquie +=j
        print(uniquie)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
