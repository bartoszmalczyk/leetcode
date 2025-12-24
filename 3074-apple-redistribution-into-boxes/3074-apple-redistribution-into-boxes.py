class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)
        all_apples = sum(apple)
        ans = 0
        for box in capacity:
            all_apples -= box
            ans += 1
            if all_apples <= 0:
                return ans
            