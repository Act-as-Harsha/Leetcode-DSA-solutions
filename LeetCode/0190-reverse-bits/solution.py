# Time Complexity: O(32) = O(1)
# Space Complexity: O(1)
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = ""
        for i in range(31, -1, -1):
            if (n&(1<<i)):
                ans+='1'
            else:
                ans+='0'
        ans = ans[::-1]
        return int(ans, 2)
