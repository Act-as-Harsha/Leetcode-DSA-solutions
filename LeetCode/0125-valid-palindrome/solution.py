class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [ch.lower() for ch in s if ch.isalnum()]

        left, right = 0, len(filtered)-1
        while left < right:
            if filtered[left] != filtered[right]:
                return False
            left += 1
            right -= 1
        return True
