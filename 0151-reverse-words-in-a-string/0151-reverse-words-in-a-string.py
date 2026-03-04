class Solution:
    def reverseWords(self, s: str) -> str:
        arr_s=s.split()
        new_s=[]
        for i in range(-1 ,-(len(arr_s)+1),-1):
            new_s.append(arr_s[i])

        reverse_s=" ".join(new_s)
        return reverse_s

