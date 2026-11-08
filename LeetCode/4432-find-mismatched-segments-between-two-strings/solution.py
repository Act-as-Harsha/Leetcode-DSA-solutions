class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        ans = []
        i = 0
        n = len(s1)
        while i < n:
            if s1[i] != s2[i]:
                start = i
                while i < n and s1[i] != s2[i]:
                    i+=1
                ans.append([s1[start:i],s2[start:i]])
            else:
                i+=1
        return ans
