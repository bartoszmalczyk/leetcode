class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        candidate1, count1 = None, 0
        candidate2, count2 = None, 0

        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1            
        if nums.count(candidate1) >= nums.count(candidate2):
            return candidate1
        else:
            return candidate2
