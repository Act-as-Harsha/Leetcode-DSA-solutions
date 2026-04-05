class Solution:
    def mirrorFrequency(self, s: str) -> int:
        from collections import Counter

        freq = Counter(s)
        visited = set()
        total = 0

        for c in freq:
            if c in visited:
                continue
            if c.isalpha():
                m = chr(ord('z') - (ord(c)-ord('a')))
            else:
                m = chr(ord('9')-(ord(c)-ord('0')))
            visited.add(c)
            visited.add(m)

            total += abs(freq[c]-freq[m])
        return total
