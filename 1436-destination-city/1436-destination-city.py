from collections import defaultdict
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hm = defaultdict(str)
        for city, destination in paths:
            hm[city] = destination
        key = paths[0][0]
        while hm[key] != "":
            key = hm[key]
        return key
