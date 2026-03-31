class Solution:
    def convertToTitle(self, col_num: int) -> str:
        result = ""
        while col_num > 0:
            col_num -= 1
            result += chr(col_num % 26 + ord("A"))
            col_num //= 26

        return result[::-1]

