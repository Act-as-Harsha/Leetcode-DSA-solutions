class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0
        for _ in range(32):
            last_bit = n & 1
            reverse = reverse << 1
            reverse |= last_bit
            n = n>>1
        return reverse

        
