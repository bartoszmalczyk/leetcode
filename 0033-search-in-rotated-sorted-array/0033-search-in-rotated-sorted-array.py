class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target: return mid
            # [4,5,6,7,0,1,2]
            if nums[l] <= nums[mid]: #left half is sorted
                if nums[mid] >= target and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
                # [7,0,1,2,4,5,6]
            elif nums[r] >= nums[mid]: #right side is sorted
                if nums[mid] <= target and nums[r] >= target:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1



