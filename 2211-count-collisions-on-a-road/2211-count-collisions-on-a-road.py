from collections import deque 

class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = deque([])
        ans = 0
        for car in directions:
            if car == "R":
                stack.append("R")
            if car == "L":
                if not stack: 
                    continue
                elif stack:
                    if stack[-1] == "S":
                        ans += 1
                    elif stack[-1] == "R":
                        ans +=2
                        stack.pop()
                        while stack and stack[-1] == "R":
                            ans += 1
                            stack.pop()
                    stack.append("S")
            elif car == "S":
                while stack and stack[-1] == "R":
                    ans +=1 
                    stack.pop()
                stack.append("S")         
        return ans
