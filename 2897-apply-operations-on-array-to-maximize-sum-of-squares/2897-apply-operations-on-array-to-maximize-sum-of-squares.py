class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        bits = [0] * 30
        for n in nums:
            while n:
                pos = (n & -n).bit_length() - 1
                bits[pos] += 1 
                n &= n - 1
        ans = 0
        for _ in range(k):
            temp = 0 
            for i in range(len(bits) - 1, -1, -1):
                if bits[i] != 0:
                    bits[i] -= 1
                    temp += 1 << i 
            ans += temp * temp 
        return ans % (10**9 + 7)
