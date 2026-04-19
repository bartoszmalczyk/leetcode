class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        for index in range(len(nums2)):
            i = 0
            j = min(index, len(nums1) - 1)

            # We are looking for first num in nums1 such a num is the
            # smallest but satisfies num > nums2[r]
            while i <= j:
                mid = (i + j) // 2
                if nums1[mid] > nums2[index]:
                    i = mid + 1
                else:
                    ans = max(ans, index - mid)
                    j = mid - 1
        return ans
