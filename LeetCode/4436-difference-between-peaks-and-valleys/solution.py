class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        n = len(nums)
        peaks  = valley = 0
        for i in range(1, n-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                peaks += nums[i]
            elif nums[i] < nums[i-1] and nums[i] < nums[i+1]:
                valley += nums[i]
        return peaks - valley
