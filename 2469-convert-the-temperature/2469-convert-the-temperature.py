class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans = []
        c = celsius + 273.15
        f = celsius * 1.8 + 32.0
        return [c,f]