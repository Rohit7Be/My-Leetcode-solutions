import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(low: int, high: int):
            if low >= high:
                return
            
            # Pick a random pivot to avoid O(n^2) worst-case
            rand_idx = random.randint(low, high)
            nums[low], nums[rand_idx] = nums[rand_idx], nums[low]
            pivot = nums[low]
            
            # 3-way partition pointers
            lt = low      # nums[low..lt-1] < pivot
            i = low + 1   # nums[lt..i-1] == pivot
            gt = high     # nums[gt+1..high] > pivot
            
            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1
            
            # Recursively sort the < pivot and > pivot sub-arrays
            quicksort(low, lt - 1)
            quicksort(gt + 1, high)

        quicksort(0, len(nums) - 1)
        return nums
        