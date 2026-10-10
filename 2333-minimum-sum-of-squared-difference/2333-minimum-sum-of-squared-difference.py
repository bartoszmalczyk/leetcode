import heapq
from collections import Counter

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diffs = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]        

        counts = Counter(diffs)
        
        sol = [[-d, c] for d, c in counts.items() if d > 0]
        heapq.heapify(sol)
        
        while k > 0 and sol:
            curr_diff = -sol[0][0]
            curr_cnt = sol[0][1]
            heapq.heappop(sol)
            next_diff = -sol[0][0] if sol else 0
            diff_gap = curr_diff - next_diff
            
            if k >= diff_gap * curr_cnt:
                k -= diff_gap * curr_cnt
                if sol:
                    sol[0][1] += curr_cnt 
            else:
                decrease = k // curr_cnt
                remainder = k % curr_cnt
                
                if curr_diff - decrease > 0:
                    heapq.heappush(sol, [-(curr_diff - decrease), curr_cnt - remainder])
                if remainder > 0 and curr_diff - decrease - 1 > 0:
                    heapq.heappush(sol, [-(curr_diff - decrease - 1), remainder])                
                k = 0 
                
        ans = 0
        for neg_diff, count in sol:
            ans += (-neg_diff) ** 2 * count
            
        return ans
        

        
         