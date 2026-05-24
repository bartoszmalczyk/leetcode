class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        for i in range(len(timeSeries) - 1):
            f = timeSeries[i]
            s = timeSeries[i + 1]
            if f + duration <= s:
                total += duration 
            else:
                total += s - f 
        total += duration
        return total

