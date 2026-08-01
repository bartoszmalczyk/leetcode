class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        x = (set(nums2) & set(nums1))
        return -1 if not x else min(x)
