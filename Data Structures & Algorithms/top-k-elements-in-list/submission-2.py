class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        i = 0
        out = []
        output = []
        nums.sort()
        while i < len(nums):
            c = nums.count(nums[i])
            hash[nums[i]] = c
            i += c
        for v in hash.values():
            if len(out) < k:
                out.append(v)
                out.sort(reverse = True)
            else:
                if v > out[-1]:
                    out.pop()
                    out.append(v)
                    out.sort(reverse = True)
        for j , v in hash.items():
            if v in out:
                output.append(j)
        return output


