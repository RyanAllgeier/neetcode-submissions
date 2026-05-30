class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out = []
        count = deque()
        for i in range(len(nums)):
            
            if count and count[0] <= i - k:
                count.popleft()
            while count and nums[count[-1]] < nums[i]:
                count.pop()
            count.append(i)
            if i + 1 >= k:
                out.append(nums[count[0]])
        return out
            
