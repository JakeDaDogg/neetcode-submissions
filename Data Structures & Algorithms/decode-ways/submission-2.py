class Solution:

  def numDecodings(self, s: str) -> int:
    if len(s) == 1:
      return 0 if s == "0" else 1

    dp = [0 if s[-1] == "0" else 1, 1]

    for i in range(len(s) - 2, -1, -1):
      tmp = 0
      if s[i] != "0":
        tmp += dp[0]
        twonum = 10 * int(s[i]) + int(s[i + 1])
        if 10<=twonum <= 26:
          tmp += dp[1]

      dp[0], dp[1] = tmp, dp[0]

    return dp[0]
        
