class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        for i in range(n):
            k = rowShift[i] % n
            grid[i] = grid[i][k:] + grid[i][:k]
        for j in range(n):
            k = colShift[j] % n 
            column = [grid[i][j] for i in range(n)]
            column = column[k:] + column[:k]
            for i in range(n):
                grid[i][j] = column[i]
        return grid
        
