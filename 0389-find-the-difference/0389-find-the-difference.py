class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict1={}
        dict2={}
        for i in range(len(s)):
            if s[i] in dict1:
                dict1[s[i]]=dict1[s[i]]+1
            else:
                dict1[s[i]]=1
        for i in range(len(t)):
            if t[i] in dict2:
                dict2[t[i]]=dict2[t[i]]+1
            else:
                dict2[t[i]]=1
                
        for k,v in dict2.items():
            if k not in dict1.keys() or v >dict1[k]:
                return k
         

        
        
       
            

        