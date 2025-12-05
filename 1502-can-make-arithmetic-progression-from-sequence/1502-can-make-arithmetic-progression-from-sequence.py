class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        def isArtmethic(ciag):
            if len(ciag) < 2:
                return True 
            roznica = ciag[1] - ciag[0]
            for i in range(2, len(ciag)):
                if ciag[i] - ciag[i-1] != roznica:
                    return False 
            return True
        return isArtmethic(arr)
