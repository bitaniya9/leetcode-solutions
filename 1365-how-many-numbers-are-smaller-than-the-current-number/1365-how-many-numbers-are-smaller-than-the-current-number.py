class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dict1={}
        list1=[]
        for i in range(len(nums)):
            dict1[nums[i]]=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    dict1[nums[i]]=dict1[nums[i]]+1
            list1.append(dict1[nums[i]])
        return list1  
                