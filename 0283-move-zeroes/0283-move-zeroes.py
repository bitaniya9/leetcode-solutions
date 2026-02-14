class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        fast=1
        slow=0
        while fast<=len(nums)-1 and slow<=len(nums)-1:
            if nums[slow]==0 and nums[fast]!=0:
                nums[slow]=nums[fast]
                nums[fast]=0
                fast+=1 
                slow+=1
            elif(nums[slow]==0 and nums[fast]==0):
                fast+=1
            elif (nums[slow]!=0):
                slow+=1
                fast+=1
