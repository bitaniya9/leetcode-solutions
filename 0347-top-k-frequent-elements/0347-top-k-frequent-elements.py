class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicts={}
        list1=[]
        for i in range(len(nums)):
            if nums[i] in dicts:
                dicts[nums[i]]=dicts[nums[i]]+1
            else:
                dicts[nums[i]]=1
        x=0
        while x<k:
            top_key=max(dicts,key=dicts.get)
            list1.append(top_key)
            del dicts[top_key]
            x+=1
        return list1

        
        

        