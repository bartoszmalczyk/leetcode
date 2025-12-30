class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l, r = 0, len(s)
        res = []

        for c in s:
            if c == "I":
                res.append(l)
                l += 1
            else:
                res.append(r)
                r -= 1
        if s[-1] == "I": res.append(l)
        else: res.append(r)
        return res