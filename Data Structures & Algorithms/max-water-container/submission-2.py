class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1
        highest_area = 0
        while left < right:
            area = (right - left) * min(heights[left],heights[right])
            highest_area = max(area,highest_area)
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        return highest_area