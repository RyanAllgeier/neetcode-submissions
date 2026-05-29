class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import defaultdict, Counter
        count = defaultdict(int)
        count_s1 = defaultdict(int)
        left = 0
        for c in s1:
            count_s1[c] += 1
        for i in range(len(s2)):
            count[s2[i]] += 1
            if i - left + 1 > len(s1):
                count[s2[i-len(s1)]] -= 1
                if count[s2[i-len(s1)]] == 0:
                    del count[s2[i-len(s1)]]
                left += 1
            if count == count_s1:
                return True
        return False

            
