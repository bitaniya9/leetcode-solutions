class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        i=0
        dict1={}
        list1=[]
        while i in range(len(s)):
            if s[i:10+i] in dict1 and len(s[i:10+i])==10:
                dict1[s[i:10+i]]=dict1[s[i:10+i]]+1
            elif (s[i:10+i] not in dict1 and len(s[i:10+i])==10):
                dict1[s[i:10+i]]=1
            i+=1
        for k,v in dict1.items():
            if v >1:
                list1.append(k)
        return list1