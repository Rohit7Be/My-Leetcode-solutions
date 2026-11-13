class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        def rev(nums,L,R):
            while L<R:
                nums[L],nums[R] = nums[R], nums[L]
                L+=1
                R-=1
        
        rev(nums,n-k,n-1)
        rev(nums,0,n-k-1)
        rev(nums,0,n-1)
        


        