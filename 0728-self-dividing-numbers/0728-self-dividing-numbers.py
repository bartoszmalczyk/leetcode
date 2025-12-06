class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right + 1):
            if "0" in str(i): 
                continue 

            divisable = True    
            for j in str(i):
                if i % int(j) != 0: 
                    divisable = False
                    break
            if divisable: 
                ans.append(i)
        return ans
                
