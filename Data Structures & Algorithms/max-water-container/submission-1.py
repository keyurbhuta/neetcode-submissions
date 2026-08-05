class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        maxarea=0
        right=len(heights)-1
        while left<right:
            area=(right-left)*min(heights[left], heights[right])
            maxarea=max(area, maxarea)
            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1
        return maxarea