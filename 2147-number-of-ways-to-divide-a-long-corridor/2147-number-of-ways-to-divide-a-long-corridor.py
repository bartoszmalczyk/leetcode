import math

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seats = []
        for i in range(len(corridor)):
            if corridor[i] == "S":
                seats.append(i)
        seats_number = len(seats)
        if seats_number % 2 != 0 or seats_number == 0:
            return 0

        sections = []
        spaces = 1
        for j in range(0,len(seats) - 1):
            if j % 2 != 0:
                end = seats[j]
                start = seats[j+1]
                spaces *= (start - end)
        return spaces % (10**9 + 7)

            