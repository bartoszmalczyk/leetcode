class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = []
        for i in range(len(score)):
            temp.append((score[i], i))
        temp.sort(key=lambda x: x[0], reverse=True)
        result = [""] * len(score)
        
        for i, (scr, original_index) in enumerate(temp):
            if i == 0:
                result[original_index] = "Gold Medal"
            elif i == 1:
                result[original_index] = "Silver Medal"
            elif i == 2:
                result[original_index] = "Bronze Medal"
            else:
                result[original_index] = str(i + 1)
        return result