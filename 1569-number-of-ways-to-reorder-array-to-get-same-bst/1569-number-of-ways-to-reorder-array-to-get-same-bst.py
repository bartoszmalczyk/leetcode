import math
class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        def help(array):
            if len(array) < 3:
                return 1
            root = array[0]
            left = []
            right = []
            for num in array:
                if num < root:
                    left.append(num)
                elif num > root: 
                    right.append(num)
            l = len(left)
            r = len(right)
            return math.comb(l + r, l) * help(left) * help(right)
        return (help(nums) - 1) % (10**9 + 7)
            
