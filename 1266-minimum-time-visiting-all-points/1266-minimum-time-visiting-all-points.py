class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for i in range(len(points) - 1):
            curr = (points[i][0], points[i][1]) 
            nxt = (points[i+1][0], points[i+1][1])
            height_diff = abs(curr[1] - nxt[1])
            width_diff = abs(curr[0] - nxt[0])
            time += min(height_diff, width_diff)
            time += abs(height_diff - width_diff)
        return time

            
            