from collections import defaultdict
from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        ans = [0]
        amount_of_each_letter = defaultdict(int)
        for letter in letters:
            amount_of_each_letter[letter] += 1

        pre_comp = []
        for wrd_index in range(len(words)):
            temp = []
            used_letters = []
            word_score = 0
            for letter in words[wrd_index]:
                word_score += score[ord(letter) - 97]
                used_letters.append(letter)
            temp.append(word_score)
            temp.append(used_letters)
            pre_comp.append(temp)

        def backtracking(step, current_score):
            if step == len(words):
                ans[0] = max(ans[0], current_score)
                return
            backtracking(step + 1, current_score)
            curr = pre_comp[step]
            valid = True
            for letter in curr[1]:
                amount_of_each_letter[letter] -= 1
                if amount_of_each_letter[letter] < 0:
                    valid = False
            if valid:
                backtracking(step + 1, current_score + curr[0])

            for letter in curr[1]:
                amount_of_each_letter[letter] += 1

        backtracking(0, 0)
        print(ans[0])
        return ans[0]