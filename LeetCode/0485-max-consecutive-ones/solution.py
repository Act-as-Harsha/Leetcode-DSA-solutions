class Solution:
    def findMaxConsecutiveOnes(self, a: list[int]) -> int:
        max_length = 0
        c = 0
        for i in range(len(a)):
            if a[i] == 1:
                c +=1
                max_length = max(max_length, c)
            else:
                c = 0
        max_length = max(max_length, c)
        return max_length
