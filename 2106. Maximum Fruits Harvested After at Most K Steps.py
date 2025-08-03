class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n=len(fruits)
        sum=[0]*(n+1)
        ind=[0]*n
        for i in range(n):
            sum[i+1]=sum[i]+fruits[i][1]
            ind[i]=fruits[i][0]
        ans=0
        for x in range(k//2+1):
            y=k-2*x
            l=startPos-x
            r=startPos+y
            st=bisect_left(ind,l)
            ed=bisect_right(ind,r)
            ans=max(ans,sum[ed]-sum[st])
            y=k-2*x
            l=startPos-y
            r=startPos+x
            st=bisect_left(ind,l)
            ed=bisect_right(ind,r)
            ans=max(ans,sum[ed]-sum[st])
        return ans        
