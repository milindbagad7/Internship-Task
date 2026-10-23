# Piling Up!
# https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true
from collections import deque

def solve():
    # Read number of test cases
    T = int(input())
    
    for _ in range(T):
        n = int(input())
        # Read the blocks into a double-ended queue for efficient ends-removal
        blocks = deque(map(int, input().split()))
        
        # Initialize top with infinity so the very first block can always be placed
        top = float('inf')
        can_stack = True
        
        while blocks:
            # Compare the leftmost and rightmost blocks
            if blocks[0] >= blocks[-1]:
                # Pick the larger element from the left if it fits on the top
                if blocks[0] <= top:
                    top = blocks.popleft()
                else:
                    can_stack = False
                    break
            else:
                # Pick the larger element from the right if it fits on the top
                if blocks[-1] <= top:
                    top = blocks.pop()
                else:
                    can_stack = False
                    break
                    
        # Print the final result for the current test case
        if can_stack and not blocks:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    solve()
