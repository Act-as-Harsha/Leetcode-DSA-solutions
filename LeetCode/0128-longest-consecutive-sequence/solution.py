class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for i in numset:
            if i - 1 not in numset:
                c = i
                s = 1
                while c + 1 in numset:
                    c += 1
                    s += 1
                longest = max(longest, s)
        return longest

