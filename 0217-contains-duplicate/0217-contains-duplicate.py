class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dicts={}
        for i in range(len(nums)):
            if nums[i] in dicts:
                return True
            else:
                dicts[nums[i]]=1
        else:
            return False
