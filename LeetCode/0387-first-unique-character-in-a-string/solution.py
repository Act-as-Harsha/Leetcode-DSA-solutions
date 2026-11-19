# Time Complexity = O(n)
# Space Complexity = O(n)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = {}
        for i in s:
            hm[i] = hm.get(i, 0) + 1
        for i in range(len(s)):
            if hm[s[i]] == 1:
                return i 
                break
        return -1
