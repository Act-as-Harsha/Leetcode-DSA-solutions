# Time complexity:O(n)
# Space complexity:O(n)
class Solution:
    def assignUmbrella(self, arr: list[int]) -> list[str]:
        r = []
        a=b=0
        for i in range(len(arr)):
            if i < len(arr)-1 and arr[i]==1 and arr[i+1]==1:
                if a<=b:
                    r.append("Alice")
                    a+=1
                else:
                    r.append("Bob")
                    b+=1
            elif arr[i]==1:
                r.append("Bob")
                b+=1
            else:
                r.append("None")
        return r
