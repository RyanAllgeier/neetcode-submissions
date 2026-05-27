class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0 
        right = len(nums) - 1
        while True:
            if target == nums[left] + nums[right]:
                return [left + 1,right + 1]
            elif target >= nums[left] + nums[right]:
                left += 1
            elif target <= nums[left] + nums[right]:
                right -= 1