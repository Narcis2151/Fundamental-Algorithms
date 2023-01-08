class Solution:
    def longestCommonSubsequence(self, text1, text2):
        n = len(text1)
        m = len(text2)
        dp=[[0 for i in range(m+1)] for j in range(n+1)]
        ans=0
        for i in range(1, n+1):
            for j in range(1, m+1):

                if text1[i-1]==text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]

                else:
                    dp[i][j]=max(dp[i][j-1], dp[i-1][j])
                ans=max(ans,dp[i][j])
        return ans

sol = Solution()
print(sol.longestCommonSubsequence("abcde", "ace" ))