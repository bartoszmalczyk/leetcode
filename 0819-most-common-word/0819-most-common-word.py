import re
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r'\w+', paragraph.lower())
        banned_set = set(banned)
        valid_words = [word for word in words if word not in banned_set]
        word_counts = Counter(valid_words)
        return word_counts.most_common(1)[0][0]