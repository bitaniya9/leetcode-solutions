class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1={}
        dict2={}
        common=[]
        intersection=""
        for i in range(len(nums1)):
            if nums1[i] in dict1:
                dict1[nums1[i]]=dict1[nums1[i]] +1
            else:
                dict1[nums1[i]]=1
        for i in range(len(nums2)):
            if nums2[i] in dict2:
                dict2[nums2[i]]=dict2[nums2[i]] +1
            else:
                dict2[nums2[i]]=1
        for k,v1 in dict1.items():
            if k in dict2.keys():
                v2=dict2[k]
                count=min(v1,v2)
                common.extend([k]*count)
        return common