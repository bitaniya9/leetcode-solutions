class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr_s=s.split()
        last_word=arr_s[len(arr_s)-1]
        return len(last_word)