from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def compare(a, b):
            stra, strb = str(a), str(b)
            if stra + strb > strb + stra:
                return -1 
            elif stra + strb < strb + stra:
                return 1
            else: 
                return 0 
        nums.sort(key=cmp_to_key(compare))
        nums = [str(x) for x in nums]
        ans = "".join(nums)
        return ans if ans.count("0") != len(ans) else "0"