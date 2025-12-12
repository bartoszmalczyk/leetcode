class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        n = len(boxes)
        for i in range(n):
            temp = 0
            for j in range(n):
                if i != j and boxes[j] == '1':
                    temp += abs(i - j)
            ans.append(temp)
        return ans