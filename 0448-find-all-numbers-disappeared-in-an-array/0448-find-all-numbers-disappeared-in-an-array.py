class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dicts={}
        list1=[]
        for i in range(len(nums)):
            if nums[i] in dicts:
                dicts[nums[i]]=dicts[nums[i]]+1
            dicts[nums[i]]=1
        for i in range(len(nums)+1):
            if i not in dicts and i!=0:
                list1.append(i)
        return list1