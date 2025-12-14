class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seats = []
        for i in range(len(corridor)):
            if corridor[i] == "S":
                seats.append(i)
        seats_number = len(seats)
        if seats_number % 2 != 0 or seats_number == 0:
            return 0
        spaces = 1
        for j in range(0,len(seats) - 1):
            if j % 2 != 0:
                spaces *= (seats[j+1] - seats[j])
        return spaces % (10**9 + 7)

            