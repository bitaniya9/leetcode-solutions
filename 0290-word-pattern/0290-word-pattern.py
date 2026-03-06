class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict1={}
        dict2={}
        new_s=s.split()
        if len(new_s) !=len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in dict1:
                if dict1[pattern[i]]!=new_s[i]:
                    return False
                    break
            if new_s[i] in dict2:
                if dict2[new_s[i]]!=pattern[i]:
                    return False
                    break
            dict1[pattern[i]]=new_s[i]
            dict2[new_s[i]]=pattern[i]
        else:
            return True
    