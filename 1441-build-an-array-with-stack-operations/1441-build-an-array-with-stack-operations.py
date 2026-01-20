from typing import List
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        for i in range(1, target[-1] + 1):
            stack.append('Push') #we always push the elemet
            if i not in target:
                stack.append('Pop') #if it s not needed we pop it
        return stack




            
        