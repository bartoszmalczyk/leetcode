from collections import defaultdict
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hm = defaultdict(int)
        ans = []
        for word in words:
            hm[word] += 1
        hm = sorted(hm.items(), key=lambda x: (-x[1], x[0]))    
        for i in range(k):
            ans.append(hm[i][0])
        return ans
            
