class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        tails = [0]*len(nums)
        size = 0

        for x in nums:
            i,j = 0, size
            while i!=j:
                mid = (i+j) // 2
                if tails[mid] < x:
                    i = mid + 1
                else:
                    j = mid
            tails[i] = x
            size = max(i+1, size)
        return size