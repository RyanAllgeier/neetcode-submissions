class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        k = 1
        m = 0
        for i in range(len(nums)):
            if i + 2 <= len(nums):
                if nums[i] + 1 == nums[i+1]:
                    k += 1
                else:
                    m = max(m,k)
                    k = 1
        if len(nums) == 0:
            return 0
        return max(m,k)
           
        



        