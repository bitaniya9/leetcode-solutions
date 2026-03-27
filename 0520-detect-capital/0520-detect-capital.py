class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0].isupper():
            for i in range(1,len(word)-1):
                if word[i].islower() and word[i+1].isupper():
                    return False
                elif word[i].isupper() and word[i+1].islower():
                    return False
                
            else:
                return True
        else:
            for i in range(len(word)-1):
                if word[i].islower() and word[i+1].isupper():
                    return False
            else:
                return True



        