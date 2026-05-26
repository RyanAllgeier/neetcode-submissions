class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       
        hash = {}
        for i, s in enumerate(strs):
            temp = s
            s = sorted(s)
            s = "".join(s)
            if hash.get(s) != None:
                tempy = hash[s]
                tempy.append(temp)
                hash[s] = tempy
            else:
                hash[s] = [temp]
        output = []
        for v in hash.values():
            output.append(v)
        return output
        

