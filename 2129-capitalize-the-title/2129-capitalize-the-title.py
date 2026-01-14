class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split()
        ans = ""
        for word in title:
            temp = word
            if len(word) in {1,2}:
                ans += temp.lower()
            else:
                temp = temp.lower()
                temp = temp[0].upper() + temp[1:]
                ans+= temp
            ans += " "
        return ans[:len(ans) - 1]