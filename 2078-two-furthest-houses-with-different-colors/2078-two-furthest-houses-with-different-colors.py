class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l,r = 0, len(colors) - 1
        if colors[l] != colors[r]:
            return r - l 
        f = l
        while f < len(colors) and colors[f] == colors[r]:
            f += 1
        e = r
        while e >= 0 and colors[e] == colors[l]:
            e -= 1

        return max(r - f, e - l)