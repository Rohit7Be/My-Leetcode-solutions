class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #here we need 2 functions to solve it using merge sort

        def merge(left,right): #this func is for merging 2 sorted arr.
            res = []
            i = 0
            j= 0

            while i<len(left) and j < len(right): 
                if left[i] <= right[j]:
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    j+=1
            while i < len(left):
                res.append(left[i])
                i +=1

            while j < len(right):
                res.append(right[j])
                j+=1

            return res
        
        def mergesort(arr): #this func will divide the arr into parts and recursion occurs here
            if len(arr) <= 1:
                return arr

            mid = len(arr)//2

            left = mergesort(arr[:mid])
            right = mergesort(arr[mid:])

            return merge(left,right) 

        return mergesort(nums)

                