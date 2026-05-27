class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s_lower = set()
        s_upper = set()
        s_valid = set()
        s_forbidden = set() 

        for char in word:
            if char.islower():
                if char.upper() in s_upper:
                    s_forbidden.add(char)
                s_lower.add(char)
            else:
                s_upper.add(char)
                if char.lower() in s_lower:
                    s_valid.add(char.lower())
                    
        return len(s_valid - s_forbidden)