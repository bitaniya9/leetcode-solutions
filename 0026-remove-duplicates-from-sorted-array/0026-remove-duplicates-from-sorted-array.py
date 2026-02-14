class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        fast=1
        slow=0
        while fast<=len(nums)-1 and slow<=len(nums)-1:
            if nums[slow]==nums[fast]:
                fast+=1
            else:
                slow+=1
                nums[slow]=nums[fast]
        slow+=1
        return slow
        