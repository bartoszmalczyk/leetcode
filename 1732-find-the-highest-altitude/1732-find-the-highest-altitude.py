class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0 
        highest = 0
        for point in gain:
            curr += point
            highest = max(curr, highest)
        return highest
        
