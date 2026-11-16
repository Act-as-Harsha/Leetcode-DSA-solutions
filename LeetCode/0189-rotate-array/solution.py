# Time Complexity  : O(n)
# Space Complexity : O(1)
class Solution:
    def rotate(self, a: list[int], k: int) -> None:
        n = len(a)
        k %=n
        a.reverse()
        a[:k]=reversed(a[:k])
        a[k:]=reversed(a[k:])
