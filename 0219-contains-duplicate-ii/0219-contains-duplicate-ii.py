class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        Nset = set()

        for i in range(len(nums)):
            if i>k:
                Nset.remove(nums[i-k-1])
            if nums[i] in Nset:
                return True
                
            Nset.add(nums[i])

        return False