class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        r1 , r2 = set(nums1) , set(nums2)
        return [list(r1-r2), list(r2-r1)]