class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ans = 0
        for fruit in fruits:
            for i in range(len(baskets)):
                if baskets[i] >= fruit:
                    baskets[i] = -1
                    break
                if i == len(baskets) - 1 and baskets[i] < fruit:
                    ans+=1
        return ans