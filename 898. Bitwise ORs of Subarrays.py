class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans=set()
        cur={0}
        for x in arr:
            cur={x|y for y in cur}|{x}
            ans|=cur
        return len(ans)       
        
