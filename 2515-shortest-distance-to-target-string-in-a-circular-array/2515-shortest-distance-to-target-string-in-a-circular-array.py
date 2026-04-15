class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        start = words[startIndex]
        n = len(words)
        l_steps = 0
        r_steps = 0
        if words[startIndex] == target: return 0
        for i in range(1, max(abs(startIndex - n), abs(startIndex))):
            l = words[(startIndex - i ) % n]
            r = words[(startIndex + i) % n] 
            l_steps += 1
            r_steps += 1

            if l == target:
                return l_steps
            if r == target:
                return r_steps
        return -1