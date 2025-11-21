class Solution:
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key=lambda x:  (x[1], -x[0]))
        #first we look for the smallest x[1] and put it in ascending order
        #if 1st elements are equals, we look at -x[0], so we just get the
        #intervals which ends first at the start
        first, second = -1, -1
        ans = 0
        for a,b in intervals:
            if a <= second:
                continue
            elif a == first:
                ans += 1
                first, second = b, a
            elif a > first:
                ans += 2
                first, second = b, b - 1
            else:
                ans += 1
                first, second = b, first
        return ans