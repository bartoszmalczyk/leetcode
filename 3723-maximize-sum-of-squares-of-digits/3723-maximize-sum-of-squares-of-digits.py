class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        s = ["0"] * num
        counter = 0 
        while sum and counter < num:
            if sum > 9:
                s[counter] = "9" 
                sum -= 9
            else:
                s[counter] = str(sum)
                sum = 0
            counter += 1
        if sum != 0:
            return ""
        else:
            return "".join(s)