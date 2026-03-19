import numpy as np 
class Solution:
    def convertToBase7(self, num: int) -> str:
        return str(np.base_repr(num, base = 7))