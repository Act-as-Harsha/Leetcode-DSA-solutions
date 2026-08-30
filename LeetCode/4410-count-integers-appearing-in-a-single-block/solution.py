class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        c = 0
        for i in set(nums):
            first = nums.index(i)
            last = len(nums) - 1 - nums[::-1].index(i)
            if last - first + 1  == nums.count(i):
                c += 1
        return c
