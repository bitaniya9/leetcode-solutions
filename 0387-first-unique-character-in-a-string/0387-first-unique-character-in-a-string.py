class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts={}
        for i in range(len(s)):
            if s[i] in counts:
                counts[s[i]]=counts[s[i]]+1
            else:
                counts[s[i]]=1
        for k,v in counts.items():
            if v==1:
                return s.index(k)
                break
        else:
            return -1
        