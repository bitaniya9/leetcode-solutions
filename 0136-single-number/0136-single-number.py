class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict1={}
        for i in range(len(nums)):
            if nums[i] in dict1:
                dict1[nums[i]]=dict1[nums[i]]+1
            else:
                dict1[nums[i]]=1
            
        for k,v in dict1.items():
            if v ==1:
                return k

        