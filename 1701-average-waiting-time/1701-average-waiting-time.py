from typing import List
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waiting = 0 
        last_finish = customers[0][0]
        for arrival, time in customers:
            extra_time = 0
            if last_finish <= arrival:
                waiting += time
            else:
                extra_time = last_finish - arrival
                waiting += time + extra_time

            if last_finish < arrival:
                last_finish = arrival + time
            else:
                last_finish += time
        return waiting / len(customers)

