class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1={}
        dict2={}
        if len(magazine)<len(ransomNote):
            return False
        for i in range(len(ransomNote)):
            if ransomNote[i] in dict1:
                dict1[ransomNote[i]]= dict1[ransomNote[i]]+1
            else:
                dict1[ransomNote[i]]=1

        for i in range(len(magazine)):
            if magazine[i] in dict2:
                dict2[magazine[i]]= dict2[magazine[i]]+1
            else:
                dict2[magazine[i]]=1
        
        for k,v in dict1.items():
            if k not in dict2 or dict2[k]<v:
                return False
        else:
            return True
           
        
