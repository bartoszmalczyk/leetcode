class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        ans = []
        temp = sentence.split()
        for i in range(len(temp)):
            if temp[i][0].lower() in vowels:
                temp[i] += "ma"
            else:
                x = temp[i][0]
                temp[i] = temp[i][1:]
                temp[i] += x
                temp[i] += "ma"
            temp[i] += (i + 1) * "a"
        return " ".join(temp)