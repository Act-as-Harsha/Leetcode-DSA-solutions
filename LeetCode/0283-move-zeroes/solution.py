# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                if i!=p1:
                    nums[p1],nums[i] = nums[i], nums[p1]
                p1+=1
        
