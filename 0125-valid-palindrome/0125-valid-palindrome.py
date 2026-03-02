import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s=re.sub(r'[^a-zA-Z0-9\s]','',s).replace(" ","")
        normalized_string = new_s.lower().strip()
        i=0
        right=len(normalized_string)-1
        left=0
        while i <len(normalized_string):
            if normalized_string[right]==normalized_string[left]:
                right-=1
                left+=1
            else:
                return False
            if right==left:
                break
            i+=1
        return True
          