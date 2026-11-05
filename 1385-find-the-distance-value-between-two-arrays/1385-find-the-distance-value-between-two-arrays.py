class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        
        def findClosest(arr, k):
            res = arr[0]
            lo = 0
            hi = len(arr) - 1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if abs(arr[mid] - k) < abs(res - k):
                    res = arr[mid]
                elif abs(arr[mid] - k) == abs(res - k):
                    res = max(res, arr[mid])

                if arr[mid] == k:
                    return arr[mid]
                elif arr[mid] < k:
                    lo = mid + 1
                else:
                    hi = mid - 1

            return res
        
        ans = 0         
        for num in arr1:
            closest_val = findClosest(arr2, num)
            if abs(num - closest_val) > d: 
                ans += 1 
                
        return ans
            

