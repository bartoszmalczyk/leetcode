class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ans = 0
        for i in fruits:
            for j in range(len(baskets)):
                if baskets[j] >= i:
                    baskets[j] = -1
                    ans += 1
                    break
        return len(fruits) - ans
