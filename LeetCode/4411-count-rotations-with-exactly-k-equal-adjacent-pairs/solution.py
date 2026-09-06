class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)
        a = 0
        for i in range(n):
            r = s[i:] + s[:i]
            score = 0
            for j in range(n-1):
                if r[j] == r[j+1]:
                    score += 1
            if score == k:
                a += 1
        return a
         
