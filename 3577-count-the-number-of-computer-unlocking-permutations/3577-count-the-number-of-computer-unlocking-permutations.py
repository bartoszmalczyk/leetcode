class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        for i in range(1,n):
            if complexity[i] > complexity[0]:
                continue
            else: 
                return 0

        n_perms, mod = 1, 10 ** 9 + 7
        for i in range(2, n):
            n_perms = n_perms * i % mod
        return n_perms