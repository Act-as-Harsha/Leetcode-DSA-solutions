#Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def frequencySort(self, s: str) -> str:
        hm = {}
        for i in s:
            hm[i] = hm.get(i, 0) + 1
        r = ""
        maxi = max(hm.values())
        while maxi > 0:
            for i in hm:
                if hm[i] == maxi:
                    r += i * maxi
            maxi -= 1
        return r
