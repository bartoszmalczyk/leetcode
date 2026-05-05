from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False
        letters = "abcdefghijklmnoprstuwqvxyz"
        hm1 = dict()
        hm2 = dict()
        for letter in letters:
            hm1[letter] = 0
            hm2[letter] = 0

        for char in s1:
            hm1[char] += 1
             
        for index in range(0, n1):
            hm2[s2[index]] += 1
        if hm1 == hm2:
            return True
        for index in range(n1, n2):
            hm2[s2[index]] += 1
            hm2[s2[index - n1]] -= 1
            if hm1 == hm2:
                return True
        return False

"""
s1 = "ab", s2 = "eidbaooo"
"""