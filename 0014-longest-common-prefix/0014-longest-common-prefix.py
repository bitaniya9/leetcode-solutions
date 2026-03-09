class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minimum_len = min(len(s) for s in strs)
        strs.sort()
        if len(strs)<2:
            return strs[0]
        
        i = 0
        cmmn_prefix = ""
        while i in range(minimum_len):
            if strs[0][i] == strs[len(strs) - 1][i]:
                cmmn_prefix += strs[0][i]
                i += 1
                if i ==minimum_len:
                    break
            else:
                break
        return cmmn_prefix
