#Time complexity:O(n)
#spacecomplexity:O(1)
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        s = sum(nums)
        l = len(nums)
        n = (l*(l+1))//2
        return n - s
        
        
