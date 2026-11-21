#Timecomplexity:O(1)
#Spacecomplexity:O(1)
class Solution:
    def minRange(self, a: int, b: int, c: int) -> int:
        def get_range(a,b,c):
            return max(a, b, c) - min(a, b, c)
        return min(
            get_range(a,b,c),
            get_range(b+c,b,c),
            get_range(a, a+c,c),
            get_range(a,b,a+b)
        )
        
