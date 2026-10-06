class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        open_brackets = 0 
        for i in s:
            if i == '(':
                open_brackets += 1
            else:
                if open_brackets:
                    open_brackets -= 1
                else:
                    ans += 1
        ans += open_brackets
        return ans
