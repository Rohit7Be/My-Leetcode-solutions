class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)): #iterate through nums
            if nums[i] >= target:
                return i
            
        
        return len(nums) #if all the vals are done iterating and still no place found, then its the last position