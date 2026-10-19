class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        s = 0
        while x > 0:
            r = x % 10
            s = s * 10 + r
            x = x//10
        return True if s==temp else False

        
