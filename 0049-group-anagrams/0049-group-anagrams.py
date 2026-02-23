class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts={}
        list1=[]
        for i in range(len(strs)):
            key="".join(sorted(strs[i]))  
            if key in dicts:
                dicts[key].append(strs[i])
            else:
                dicts[key]=[strs[i]]
        for k,v in dicts.items():
            list1.append(v)
        return list1