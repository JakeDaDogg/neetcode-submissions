class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1, 0]

        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                # No valid decoding starts with '0'
                tmp = 0
            else:
                # 1-digit mapping is always valid for '1'-'9'
                tmp = dp[0]
                
                # 2-digit mapping is valid if we aren't at the last char and it's <= 26
                if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                    tmp += dp[1] 
            
            # Shift the DP variables backward
            dp[0], dp[1] = tmp, dp[0]
        
        return dp[0]