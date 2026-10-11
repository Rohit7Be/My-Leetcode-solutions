class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        fir = sec = float('inf')

        for i in nums:
            if i<=fir:
                fir = i
            elif i<=sec:
                sec=i
            else:
                return True
        return False