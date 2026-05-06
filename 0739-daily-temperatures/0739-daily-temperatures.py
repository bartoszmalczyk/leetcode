class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []
        for index, val in enumerate(temperatures):
            while stack and stack[-1][0] < val:
                v, i = stack.pop()
                results[i] = index - i
            stack.append([val, index])

        return results

         

