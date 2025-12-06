class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 5 == 0 or k % 2 == 0: return -1
        counter = 1
        rest = 1
        while True:
            if rest % k == 0: return counter
            else: counter += 1
            rest = (10 * rest + 1 ) % k

            

            
    