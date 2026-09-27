class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans = []
        while nums:
            v = sorted(set(nums))
            for x in v:
                ans.append(x)
                nums.remove(x)
        return ans
        
        
