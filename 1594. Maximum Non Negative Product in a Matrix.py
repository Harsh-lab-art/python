class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        dp = [None] * n
        dp[0] = (grid[0][0], grid[0][0])
        for j in range(1, n):
            val = dp[j-1][0] * grid[0][j]
            dp[j] = (val, val)
        for i in range(1, m):
            for j in range(0, n):
                v = grid[i][j]
                if j == 0:
                    val = dp[j][0] * v
                    dp[j] = (val, val)
                else:
                    choices = (
                        dp[j][0] * v,  
                        dp[j][1] * v, 
                        dp[j-1][0] * v, 
                        dp[j-1][1] * v  
                    )
                    dp[j] = (max(choices), min(choices))
        max_res = dp[n-1][0]
        return max_res % MOD if max_res >= 0 else -1
