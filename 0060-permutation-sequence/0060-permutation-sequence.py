from math import factorial
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = []
        nums = [str(i) for i in range(1, n+1)]
        current_factorial = factorial(n - 1)
        k -= 1

        def recursion(nums, k, current_factorial):
            if not nums:
                return
            index = k // current_factorial
            new_k = k % current_factorial

            ans.append(nums[index])
            nums.pop(index)

            if len(nums) > 0:
                new_factorial = current_factorial // len(nums)
                recursion(nums, new_k, new_factorial)

        recursion(nums, k, current_factorial)
        return "".join(ans)

sol = Solution()
print(sol.getPermutation(5, 3))