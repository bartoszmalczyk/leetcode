import numpy as np

class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        arr_len = len(arr)
        c = 0
        s = 0
        for i in range(round(0.05 * arr_len), round(0.95 * arr_len)):
            s += arr[i]
            c += 1
        return s / c


        