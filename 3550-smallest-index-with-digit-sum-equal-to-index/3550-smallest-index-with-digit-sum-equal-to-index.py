class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sumOfDigits(num):
            if num < 10:
                return num
            temp = 0
            for i in str(num):
                temp += int(i)
            return temp 
            
        for index, val in enumerate(nums):
            if index == sumOfDigits(val):
                return index 
        return -1