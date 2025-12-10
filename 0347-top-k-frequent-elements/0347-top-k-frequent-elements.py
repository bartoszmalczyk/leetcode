from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        firstly, we create a hashmap which will store the freqency
        of each element hm = {number : freq}
        
        secondly, we make a heap and then iterate through each element
        in the hashmap hm.items() -> [(key : value)]

        we add the value we are curently on to the heap(freq, num) 
        => the tuples are sorted by the 1th not 2nd element

        if the len of the heap exceeds the number k, we pop the last 
        item = the item where freq is the lowest

        we return the most frequent numbers
        """
        hm = defaultdict(int)
        for i in nums:
            hm[i] += 1
        
        heap = []

        for number, freq in hm.items():
            heapq.heappush(heap, (freq, number))
            if len(heap) > k:
                heapq.heappop(heap)
                
        ans = []
        for _ , number in heap:
            ans.append(number)
        return ans