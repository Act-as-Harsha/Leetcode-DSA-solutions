class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set()

        for x in nums:
            if x in s:
                return True
            s.add(x)

        return False
