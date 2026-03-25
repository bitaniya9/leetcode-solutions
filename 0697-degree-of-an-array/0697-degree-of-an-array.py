class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dicts={}
        first={}
        last={}
        maxCount=0
        num_subarray = float('inf')

        for i in range(len(nums)):
            last[nums[i]]=i
            if nums[i] in dicts:
                dicts[nums[i]]=dicts[nums[i]]+1
                last[nums[i]]=i
            else:
                dicts[nums[i]]=1
                first[nums[i]]=i


        

        for k,v in dicts.items():
            maxCount=max(maxCount,v)
        for k in dicts.keys():
            if dicts[k]==maxCount:
                num_subarray=min(num_subarray,last[k]-first[k]+1)
        return num_subarray

        