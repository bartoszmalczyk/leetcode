class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn > 8: return []
        ans = []

        for hours in range(12):
            for minutes in range(60):
                if hours.bit_count() + minutes.bit_count() == turnedOn:
                    if minutes < 10:
                        ans.append(f"{hours}:0{minutes}")
                    else:
                        ans.append(f"{hours}:{minutes}")
        return ans