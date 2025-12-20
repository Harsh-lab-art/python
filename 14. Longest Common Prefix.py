class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        pre=strs[0]  
        for i in range(len(pre)):
            for word in strs[1:]:
                if i>=len(word) or word[i]!=pre[i]:
                    return pre[:i]
        return pre
