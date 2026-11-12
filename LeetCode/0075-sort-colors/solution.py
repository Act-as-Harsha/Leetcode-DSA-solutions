# Time complexity : O(n)
# Space Complexity : O(1)
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        zero = nums.count(0)
        one = nums.count(1)
        two = nums.count(2)
        i = 0 
        for _ in range(zero):
            nums[i] = 0
            i+=1
        for _ in range(one):
            nums[i] = 1
            i+=1
        for _ in range(two):
            nums[i] = 2
            i+=1
        

        
