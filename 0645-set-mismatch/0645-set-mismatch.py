class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        mismatch=[]
        counts={}
        n=len(nums)
        for i in range(0,n):
            if nums[i] in counts:
                counts[nums[i]]=counts[nums[i]]+1
            else:
                counts[nums[i]]=1
            if counts[nums[i]]>1:
                mismatch.append(nums[i])
        try:
            for i in range(1,n+1):
                counts[i]
        except KeyError:
            mismatch.append(i)
        return mismatch