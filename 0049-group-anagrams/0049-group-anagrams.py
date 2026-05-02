from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm_group = defaultdict(list)
        for string in strs:
            hm_group[str(sorted(string))].append(string)
        return list(hm_group.values())