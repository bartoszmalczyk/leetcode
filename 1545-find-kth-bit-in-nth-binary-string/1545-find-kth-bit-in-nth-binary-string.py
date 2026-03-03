class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        table = str.maketrans("01", "10")
        def creation(n):
            nonlocal table
            if n == 0: return "0"
            else:
                temp = creation(n - 1)
                return temp + "1" + temp.translate(table)[::-1]
        ans = creation(n - 1)
        return ans[k - 1]