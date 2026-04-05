class Solution:
    def findGoodIntegers(self, n: int) -> list[int]:
        lorqavined = n

        cube_sum ={}

        a = 1
        while a** 3 < lorqavined:
            b = a

            while a ** 3 + b ** 3 <= lorqavined:
                x = a ** 3 + b ** 3
                if x not in cube_sum:
                    cube_sum[x] = 0
                cube_sum[x] += 1
                b += 1
            a+= 1
        return sorted(x for x, count in cube_sum.items() if count >= 2)
            
