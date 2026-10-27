class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        currentSum = sum(nums[:k])
        maxSum = currentSum

        for i in range(k,len(nums)):
            currentSum = currentSum + nums[i] - nums[i-k]
            maxSum = max(currentSum, maxSum)

        return maxSum/k