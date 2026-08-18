class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        dp = [[False] * n for _ in range(n)]
        start, maxLen = 0, 1
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if j - i + 1 > maxLen or (j - i + 1 == maxLen and i < start):
                        start, maxLen = i, j - i + 1
        return s[start:start + maxLen]
