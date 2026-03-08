# Python3 | O(n) Time & Space | Hash Set & Base-10 Conversion

# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The problem asks us to find a binary string of length `n` that is not present in the given list. Instead of generating and comparing binary strings directly, it is much simpler to treat these strings as standard numbers. By converting the binary strings into base-10 integers, we can utilize a hash set to quickly identify which values are present and which are missing. Since there are only n strings provided, the missing number is guaranteed to be found within the range of `0` to `n`.
# Approach
<!-- Describe your approach to solving the problem. -->
1. Initialize an empty hash set `nums_set` and determine the length `n` of the binary strings.
2. Iterate through the given list nums, converting each binary string into a base-10 integer using `int(bin_str, 2)`, and store it in the set for $O(1)$ lookups.
3. First, check if `0` is missing from the set. If it is, immediately return a string of n zeros.
4. If `0` is present, start a loop to find the first missing integer. While the loop theoretically runs up to $2^{16}$, the Pigeonhole Principle guarantees we will find a missing number within at most `n + 1` iterations.
5. Once the missing integer is found, convert it back into a binary string using format(i, 'b').
6. Pad the resulting binary string with leading zeros to ensure it matches the required length `n`, and return it.

![Screenshot 2026-03-08 at 10.58.12.png](https://assets.leetcode.com/users/images/cd3b548a-1bb4-4324-a511-27a466d3bd0e_1772963911.4595957.png)

# Complexity
- Time complexity:$$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:$$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
# Code
```python3 []
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums_set = set()
        n = len(nums[0])
        for bin_str in nums:
            nums_set.add(int(bin_str, 2))
        
        if 0 not in nums_set:
            return "0" * n

        for i in range(min(nums_set), 2**16):
            if i not in nums_set:
                sol = format(i, 'b')
                break
                
        return "0" * (n - len(sol)) + sol
            
```