class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1={}
        list1=[-1]*len(nums1)
        for i in range(len(nums1)):
            if nums1[i] not in dict1:
                dict1[nums1[i]]=i
        for i in range(len(nums2)):
            if nums2[i] not in dict1:
                continue
            for j in range(i+1,len(nums2)):
                if nums2[i]<nums2[j]:
                    list1[dict1[nums2[i]]]=nums2[j]
                    break
        return list1
        