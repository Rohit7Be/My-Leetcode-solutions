class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) -1
        maxArea = 0
        while left<right:
            current = min(height[left], height[right]) * (right-left)
            maxArea = max(current,maxArea)

            if height[left]>height[right]:
                right -= 1
            else:
                left +=1
            
        return maxArea