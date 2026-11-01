class Solution:
    def majorityElement(self, a: list[int]) -> int:
        n = len(a)
        hm = {}
        for i in a:
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1
        for i in hm:
            if hm[i]>n//2:
                return i
        
