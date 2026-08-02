class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while len(nums1) > m: #remove extra vals from nums1
            nums1.pop()
        
        while len(nums2) > n: #remove extra here also
            nums2.pop()
        for k in nums2: #adding all to nums1
            nums1.append(k)

        return nums1.sort()


        