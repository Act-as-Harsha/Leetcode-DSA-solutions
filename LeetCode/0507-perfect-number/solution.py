#Time complexity : O(sqrt(n))
# space complexity : O(1)
class Solution:
    def checkPerfectNumber(self, n: int) -> bool:
        if n == 1:
            return False
        s = 1
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                s += i
                if i != n // i:
                    s += n // i
        return s == n
