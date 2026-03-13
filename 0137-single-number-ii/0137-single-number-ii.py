class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dicts={}
        for i in range(len(nums)):
            if nums[i] in dicts:
                dicts[nums[i]]+=1
            else:
                dicts[nums[i]]=1
        for k,v in dicts.items():
            if v==1:
                return k
                
        