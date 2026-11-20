# Time Complexity: O(n * klogk)
# Space Complexity: O(n * k)
class Solution:
    def groupAnagrams(self, s: list[str]) -> list[list[str]]:
        hm = {}
        for i in s:
            key = "".join(sorted(i))
            if key in hm:
                hm[key].append(i)
            else:
                hm[key] = [i]
        return list(hm.values())

        
