class Solution:
    def minimumDeletions(self, s: str) -> int:
        b = 0
        a = s.count('a')
        ans = a

        for c in s:
            if c == "a":
                a -= 1
            else:
                b += 1
            ans = min(ans, a + b)
        return ans
        

"""
"aababbab"
B's - before 
A's - after
4 - a 
4 - b

"a a b a b b a b"
[4,3,2,2,1,1,1,0,0]
"""