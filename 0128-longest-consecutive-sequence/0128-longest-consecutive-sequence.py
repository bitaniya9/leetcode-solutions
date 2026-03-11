class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1=set(nums)
        longest=0
        count=0
        for num in set1:
            if num -1 not in set1:
                current=num
                count=1
                while current + 1 in set1:
                    count+=1
                    current+=1
            longest=max(longest,count)
        return longest

            
        