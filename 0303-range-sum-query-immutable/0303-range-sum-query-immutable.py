class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [0] * len(nums)
        curr_sum = 0
        for i, num in enumerate(nums):
            curr_sum += num
            self.prefix[i] = curr_sum

    def sumRange(self, left: int, right: int) -> int:
        return (
            self.prefix[right] - self.prefix[left] + self.nums[left]
        )


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)