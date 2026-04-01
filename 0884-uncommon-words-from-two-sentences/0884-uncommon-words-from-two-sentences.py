class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        dict1={}
        dict2={}
        list1=[]
        new_s1=s1.split()
        new_s2=s2.split()
        for word in new_s1:
            if word in dict1:
                dict1[word]=dict1[word]+1
            else:
                dict1[word]=1
        for word in new_s2:
            if word in dict2:
                dict2[word]=dict2[word]+1
            else:
                dict2[word]=1
        
        for s in new_s1:
            if s not in dict2 and dict1[s]==1:
                list1.append(s)
        for s in new_s2:
            if s not in dict1 and dict2[s]==1:
                list1.append(s)
        return list1     
        
        