class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        def backTrack(start, path):
            res.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backTrack(i+1,path)
                path.pop()

        backTrack(0,[])
        return res