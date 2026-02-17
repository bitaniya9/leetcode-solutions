class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s={}
        dict_t={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in dict_s:
                dict_s[s[i]]=dict_s[s[i]]+1
            else:
                dict_s[s[i]]=1
            sorted(dict_s)
        for i in range(len(t)):
            if t[i] in dict_t:
                dict_t[t[i]]=dict_t[t[i]]+1
            else:
                dict_t[t[i]]=1
            sorted(dict_t)
        if dict_t==dict_s:
            return True
        else:
            return False