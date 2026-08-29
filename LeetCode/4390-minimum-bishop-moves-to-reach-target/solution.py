class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        rava, celi = source
        ronu, cavi = target

        if abs(rava - ronu) == abs(celi - cavi):
            return 1 
        if (rava + celi) % 2 == (ronu + cavi) % 2:
            return 2
        return -1
        
