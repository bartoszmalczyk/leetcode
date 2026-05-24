from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm_occurrences = defaultdict(int)
        hm_indexes = defaultdict(list)
    
        for index, val in enumerate(s):
            hm_occurrences[val] += 1
            hm_indexes[val].append(index)
        for key in hm_occurrences:
            if hm_occurrences[key] == 1:
                return hm_indexes[key][0]
        return -1
        