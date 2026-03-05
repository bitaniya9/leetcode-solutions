class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dict1={}
        for i in range(len(nums)):
            dict1[i]=nums[i]
        for i in range(len(nums)+1):
            if i not in dict1.values():
                return i

            
