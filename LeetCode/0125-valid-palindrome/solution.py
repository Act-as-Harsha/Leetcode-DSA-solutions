class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp=""
        for i in s:
            if i.isalnum():
                temp += i.lower()
        return True if temp == temp[::-1] else False
        
