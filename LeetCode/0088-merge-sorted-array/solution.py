class Solution:
    def merge(self, a: list[int], m: int, b: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p2 = n-1
        k = m+n-1
        while p1>=0 and p2>=0:
            if a[p1]>b[p2]:
                a[k] = a[p1]
                p1-=1
            else:
                a[k] = b[p2]
                p2-=1
            k-=1
        while p2>=0:
            a[k] = b[p2]
            p2-=1
            k-=1
        
