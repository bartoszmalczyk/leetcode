class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minimum = float('inf')
        sol = []
        print(arr)
        for i in range(len(arr) - 1):
            diff = arr[i+1] - arr[i]

            if diff < minimum:
                minimum = arr[i+1] - arr[i]
                sol.clear()
            if diff == minimum:
                temp = [arr[i], arr[i+1]]
                sol.append(temp)
        return sol
