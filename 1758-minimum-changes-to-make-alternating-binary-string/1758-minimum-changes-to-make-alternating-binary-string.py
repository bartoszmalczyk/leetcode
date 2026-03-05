class Solution:
    def minOperations(self, s: str) -> int:
        # scenario one: 10101...
        scen1 = 0
        scen2 = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != '1':
                    scen1 += 1
                else:
                    scen2 += 1
            else: 
                if s[i] != '0':
                    scen1 += 1
                else:
                    scen2 += 1
        return min(scen1, scen2)
