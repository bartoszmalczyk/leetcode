class Solution:
    def maximum69Number (self, num: int) -> int:
        temp = list(str(num))
        first_six = None
        for i in range(len(temp)):
            if temp[i] == "6":
                first_six = i
                break
        temp[i] = "9"

        return int("".join(temp))

         
