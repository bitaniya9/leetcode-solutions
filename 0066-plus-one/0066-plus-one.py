class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stopped=False
        for i in range(len(digits)-1,-1,-1):
            if(digits[i]==9):
                digits[i]=0
                continue
            if digits[i]!=9:
                digits[i]=digits[i]+1
                stopped=True
                break   
        if(stopped==False):
            digits.append(1)
            digits.reverse()
    
        return digits
        