import heapq
from collections import Counter

class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        pre = []
        max_h = []
        min_h = []
        to_remove = Counter()
        
        sum_left = sum_right = 0
        count_left = count_right = 0
        
        def clean(heap, sign):
            while heap and to_remove[sign * heap[0]] > 0:
                to_remove[sign * heap[0]] -= 1
                heapq.heappop(heap)
                
        def balance():
            nonlocal sum_left, sum_right, count_left, count_right
            clean(max_h, -1)
            clean(min_h, 1)
            
            while count_left > count_right + 1:
                val = -heapq.heappop(max_h)
                sum_left -= val
                count_left -= 1
                heapq.heappush(min_h, val)
                sum_right += val
                count_right += 1
                clean(max_h, -1)
                
            while count_left < count_right:
                val = heapq.heappop(min_h)
                sum_right -= val
                count_right -= 1
                heapq.heappush(max_h, -val)
                sum_left += val
                count_left += 1
                clean(min_h, 1)
                
            clean(max_h, -1)
            clean(min_h, 1)

        for i in range(n):
            num = nums[i]
            if not max_h or num <= -max_h[0]:
                heapq.heappush(max_h, -num)
                sum_left += num
                count_left += 1
            else:
                heapq.heappush(min_h, num)
                sum_right += num
                count_right += 1
                
            if i >= x:
                old_num = nums[i - x]
                to_remove[old_num] += 1
                if max_h and old_num <= -max_h[0]:
                    sum_left -= old_num
                    count_left -= 1
                else:
                    sum_right -= old_num
                    count_right -= 1
                    
            balance()
            if i >= x - 1:
                median = -max_h[0]
                cost = sum_right - sum_left + (count_left - count_right) * median
                pre.append(cost)

        n_pre = len(pre)
        dp = [[float('inf')] * (k + 1) for _ in range(n_pre + x + 1)]
        for i in range(len(dp)):
            dp[i][0] = 0
            
        for i in range(n_pre - 1, -1, -1):
            for j in range(1, k + 1):
                skip = dp[i + 1][j]
                take = pre[i] + dp[i + x][j - 1]
                dp[i][j] = min(skip, take)
                
        return int(dp[0][k])