class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        mod = 10**9 + 7
        c = 0
        for n in nums:
            w = n%10
            d = str(n//10)
            x = int(d[:w])
            y = int(d[w:])
            c = (c + pow(x,y,mod))%mod
        return c
        
