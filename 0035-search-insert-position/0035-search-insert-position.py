class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)): #iterate through nums
            if nums[i] == target:
                return i
            elif nums[i] < target: #if its less then continue
                continue
            else:
                return i #if not less then this is the desired position
        
        return len(nums) #if all the vals are done iterating and still no place found, then its the last position