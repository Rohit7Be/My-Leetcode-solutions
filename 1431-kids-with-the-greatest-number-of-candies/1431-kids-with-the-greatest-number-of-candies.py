class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxC = max(candies)

        res = []

        for i in candies:
            if i + extraCandies >= maxC:
                res.append(True)
            else:
                res.append(False)
        
        return res