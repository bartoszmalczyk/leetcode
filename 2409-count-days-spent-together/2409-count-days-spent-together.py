class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def calc(s: str) -> int:
            a = sum(days[:int(s[:2]) - 1])
            total = a + int(s[3:])    
            return total
        
        aa = calc(arriveAlice)
        al = calc(leaveAlice)

        ba = calc(arriveBob)
        bl = calc(leaveBob)
    
        if al < ba or bl < aa:
            return 0 
        else:
            return min(al, bl) - max(aa, ba) + 1