class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vovels = {'a', 'e', 'i', 'o','u'}
        s = s.lower()
        count1 = 0
        count2 = 0

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] in vovels:
                count1 += 1
            if s[r] in vovels:
                count2 += 1
            l += 1
            r -= 1
        return count1 == count2

    