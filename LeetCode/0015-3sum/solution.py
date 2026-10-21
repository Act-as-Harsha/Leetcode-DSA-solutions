
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            a = nums[i]

            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            if a + nums[i + 1] + nums[i + 2] > 0:
                break
            if a + nums[n - 2] + nums[n - 1] < 0:
                continue

            left, right = i + 1, n - 1

            while left < right:
                total = a + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([a, nums[left], nums[right]])
                    lv, rv = nums[left], nums[right]

                    while left < right and nums[left] == lv:
                        left += 1
                    while left < right and nums[right] == rv:
                        right -= 1

        return res

