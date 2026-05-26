class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dummy = nums.copy() #dummy list
        hold = dummy.pop(0) #hold = first element
        first = 1 
        for t in dummy: #compute product - first element
            first *= t
        output = [first]
        i = 1
        while dummy:
            if dummy[0] == 0:
                first = 1
                for j, x in enumerate(nums):
                    if j != i:
                        first *= x
                output.append(first)
                hold = dummy.pop(0)
            else:
                new = first * hold / dummy[0]
                hold = dummy.pop(0)
                output.append(int(new))
                first = new
            i += 1
        return output
            
