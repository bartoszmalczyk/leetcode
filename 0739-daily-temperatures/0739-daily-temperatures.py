class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []
        for index, val in enumerate(temperatures):
            if not stack:
                stack.append(tuple([val, index]))
            while stack[-1][0] < val:
                v, i = stack.pop()
                results[i] = index - i
                if not stack: break
            stack.append(tuple([val, index]))
        return results

         

