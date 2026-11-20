class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        hashmap = {}

        for i in range(n):
            rem = target - nums[i]
            if rem in hashmap:
                return [hashmap[rem], i]
            hashmap[nums[i]] = i