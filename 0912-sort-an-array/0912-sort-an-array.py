class Solution:

    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)

    # Correct indentation: merge is now a sibling method of sortArray
    def merge(self, L: list[int], R: list[int]) -> list[int]:
        res = []
        i, j = 0, 0
        n, m = len(L), len(R)

        while i < n and j < m:
            if L[i] < R[j]:
                res.append(L[i])
                i += 1
            else:
                res.append(R[j])
                j += 1

        # Append remaining elements
        while i < n:
            res.append(L[i])
            i += 1

        while j < m:
            res.append(R[j])
            j += 1

        return res