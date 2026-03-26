class Solution:
    def reverseWords(self, s: str) -> str:

        list1=[]
        new_s=s.split()
        for word in new_s:
            list1.append(word[::-1])
            
        return " ".join(list1)