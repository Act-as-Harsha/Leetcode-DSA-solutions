#Time complexity: 0(n)
#space complexity: o(n)
class Solution:
    def findDuplicate(self, a: list[int]) -> int:
        hm = {}
        for i in a:
            hm[i] = hm.get(i, 0) + 1
        for i in hm:
            if hm[i] > 1:
                return i
    
        
