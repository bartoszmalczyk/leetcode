class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def get_divisors_sum_if_four(n):
            divs = set()
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    divs.add(i)
                    divs.add(n // i)       
                    if len(divs) > 4:
                        return 0
            return sum(divs) if len(divs) == 4 else 0
        res = 0 
        for num in nums:
            res += get_divisors_sum_if_four(num)
        return res