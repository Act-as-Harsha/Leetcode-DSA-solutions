from typing import List

class Solution:
    def longestCommonPrefix(self, words: List[str]) -> str:
        prefix = ""
        words = sorted(words)
        first_word = words[0]
        last_word = words[-1]
        for i in range(min(len(first_word), len(last_word))):
            if first_word[i] != last_word[i]:
                return prefix
            prefix += first_word[i]
        return prefix

