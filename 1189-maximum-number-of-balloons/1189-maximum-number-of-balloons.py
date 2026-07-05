
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hm = {'b': 0, 'a' : 0, 'l':0, 'o' : 0,'n': 0}
        for letter in text:
            if letter in hm:
                hm[letter]+=1
            else:
                continue
        hm['o'] /= 2
        hm['l'] /= 2
        print(hm)
        ans = min(hm.values())
        if ans < 1: 
            return 0
        else: 
            return int(ans)