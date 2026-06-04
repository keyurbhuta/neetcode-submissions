class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea=0
        left=0
        right=len(heights)-1
        while left<right:
            area = min(heights[left], heights[right]) * (right - left)            
            maxarea=max(maxarea, area)
            if heights[right]>heights[left]:
                left+=1
            else:
                right-=1
        return maxarea