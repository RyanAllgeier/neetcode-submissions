class Solution:
    def trap(self, height: List[int]) -> int:
        w = 0
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        
        for i in range(len(height)):
            left_max = max(height[left],left_max)
            right_max = max(height[right],right_max)
            w += min(right_max,left_max) - height[i]
            if left_max <= right_max:
                left += 1
            else:
                right -= 1
        return w
        