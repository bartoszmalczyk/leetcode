class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month_aa = sum(days[:int(arriveAlice[:2]) - 1])
        alice_a = month_aa + int(arriveAlice[3:])

        month_al = sum(days[:int(leaveAlice[:2]) - 1])
        alice_l = month_al + int(leaveAlice[3:])
        print(alice_a, alice_l)

        month_ba = sum(days[:int(arriveBob[:2]) - 1])
        bob_a = month_ba + int(arriveBob[3:])

        month_bl = sum(days[:int(leaveBob[:2]) - 1])
        bob_l = month_bl + int(leaveBob[3:])
        print(bob_a, bob_l)

        # not overlapping:
        if alice_l < bob_a or bob_l < alice_a:
            return 0 
        else:
            return min(alice_l, bob_l) - max(alice_a, bob_a) + 1