class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        prev = intervals[0]
        n = len(intervals)

        for i in range(1, n):
            curr = intervals[i]
            if prev[1] >= curr[0]: # they overlap
                prev[1] = max(prev[1], curr[1])
            else:
                merged.append(prev)
                prev = curr
        merged.append(prev)
        return merged

# [[1,3],[2,6],[8,10],[15,18]]
# 1-3    8-10    15--18
#  2---6
# 
# 
# 
