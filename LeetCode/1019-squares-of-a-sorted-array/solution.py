#Timecomplexity:O(n + logn)
#Spacecomplexity:O(1)
class Solution:
    def sortedSquares(self, arr: list[int]) -> list[int]:
        for i in range(len(arr)):
            arr[i] = arr[i]**2
        return sorted(arr)
        
