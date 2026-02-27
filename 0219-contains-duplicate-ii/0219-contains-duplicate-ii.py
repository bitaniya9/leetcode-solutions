class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dicts={}
        for i in range(len(nums)):
            if nums[i] in dicts:
                distance=abs(i-dicts[nums[i]])
                if distance<=k:
                    return True
                    break
                else:
                    dicts[nums[i]]=i
            else:
                dicts[nums[i]]=i
        else:
            return False       