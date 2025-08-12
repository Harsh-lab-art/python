class Solution(object):
    def numberOfWays(self, n, x):
        mod=10**9+7
        pow=[]
        b=1
        while b ** x<=n:
            pow.append(b**x)
            b+=1
        dp=[0]*(n+1)
        dp[0]=1
        for p in pow:
            for s in range(n,p-1,-1):
                dp[s]=(dp[s]+dp[s-p])%mod
        return dp[n]            
