# Time complexity:O(n)
# Space Complexity:O(n)
class Solution:
    def majorityElement(self, arr: list[int]) -> list[int]:
        n = len(arr)
        l = []
        hm = {}
        for i in arr:
            hm[i] = hm.get(i, 0) + 1
        for i in hm:
            if hm[i] > n//3:
                l.append(i)
        return l
        
