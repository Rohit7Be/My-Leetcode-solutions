class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        maxi = float("-inf")
        total = 0
        for i in range(n):
            total = total + nums[i]
            maxi = max(total,maxi)
            if total < 0:
                total = 0
        
        return maxi