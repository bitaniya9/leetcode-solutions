class Solution:
    def reverseDegree(self, s: str) -> int:
        list1=[]
        nums=0
        for chars in s:
            value_s=27-(ord(chars)-ord('a')+1)
            list1.append(value_s)
        for i,v in enumerate(list1):
            nums+=v*(i+1)

        return nums
        