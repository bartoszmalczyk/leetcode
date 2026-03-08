class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums_set = set()
        n = len(nums[0])
        for bin_str in nums:
            nums_set.add(int(bin_str, 2))
        
        if 0 not in nums_set:
            return "0" * n

        for i in range(min(nums_set), 2**16):
            if i not in nums_set:
                sol = format(i, 'b')
                break
        return "0" * (n - len(sol)) + sol
        ans = ""
        for i in range(n - len(sol)):
            ans += "0"
        ans += sol

        return ans
            