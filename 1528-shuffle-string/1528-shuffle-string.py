class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dicts={}
        list1=[]
        for i in range(len(indices)):
            dicts[indices[i]]=s[i]
        dicts=dict(sorted(dicts.items()))
        for k,v in dicts.items():
            list1.append(v)
        list1="".join(list1)
        return list1
