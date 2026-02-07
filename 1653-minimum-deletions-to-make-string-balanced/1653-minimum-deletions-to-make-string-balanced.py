class Solution:
    def minimumDeletions(self, s: str) -> int:
        b = [0]
        a = [s.count('a')]
        ans = float('inf')
        for c in s:
            if c == 'a':
                a.append(a[-1] - 1)
                b.append(b[-1])
            else: #'b'
                b.append(b[-1] + 1)
                a.append(a[-1])
        b = b[1:]
        a.pop()
        for i in range(len(s)):
            ans = min(ans, a[i] + b[i])
        return ans - 1
            



"""
"aababbab"
B's - before 
A's - after
4 - a 
4 - b

"a a b a b b a b"
[4,3,2,2,1,1,1,0,0]
"""