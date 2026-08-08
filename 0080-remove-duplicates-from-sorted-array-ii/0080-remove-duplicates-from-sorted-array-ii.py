class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = nums[0]
        counter = 1
        position = 1
        for i in range(1, len(nums)):
            if nums[i] == last:
                counter += 1
            else:
                last = nums[i]
                counter = 1

            if counter <= 2:
                nums[position] = nums[i]
                position += 1
                
        return position
        