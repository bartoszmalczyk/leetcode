class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_ = releaseTimes[0]
        index = 0
        for i in range(1,len(releaseTimes)):
            temp = releaseTimes[i] - releaseTimes[i - 1]
            if temp > max_:
                max_ = temp
                index = i
            if temp == max_:
                if keysPressed[i] > keysPressed[index]:
                    index = i
        return keysPressed[index]