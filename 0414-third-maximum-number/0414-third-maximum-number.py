class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maximum=nums[0]
        nums.sort()
        nums.reverse()
        list1=[]
        i=0
        if len(nums)>=3:
            while i<len(nums)-1:
                if nums[i]==nums[i+1]:
                    del nums[i+1]
                else:
                    i+=1
        list1.extend(nums)
        
        if len(list1)<3:
            for i in range(len(nums)-1):
                if nums[i]<nums[i+1]:
                    maximum=nums[i+1]
                else:
                    maximum=nums[i]
            return maximum
        if len(list1)>=3:
            return list1[2]
                
            
       
        