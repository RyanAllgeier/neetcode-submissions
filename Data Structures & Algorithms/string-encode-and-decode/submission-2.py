class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for i, s in enumerate(strs):
            l = len(s)
            l = str(l)
            out += l + "#" + s
        return out


    def decode(self, s: str) -> List[str]:
        l_start = 0
        out = []
        i = 0
        while i < len(s):
            if s[i] == "#":
                l = int(s[l_start:i])
                out.append(s[i+1:i+l+1])
                l_start = i + l + 1
                i = l_start
            else:
                i += 1
        return out


