#Time complexity: O(logn)+O(n)
#space complexity:O(1)
class Solution:
    def firstMissingPositive(self, arr: list[int]) -> int:
        arr.sort()
        ans = 1
        for i in range(len(arr)):
            if arr[i] == ans:
                ans += 1
        return ans

        
