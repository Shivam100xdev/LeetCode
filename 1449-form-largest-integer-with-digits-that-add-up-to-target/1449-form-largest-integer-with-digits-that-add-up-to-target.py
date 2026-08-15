class Solution:
    def largestNumber(self, cost, target):
        dp = ["0"] * (target + 1)
        dp[0] = ""
        for t in range(1, target + 1):
            for d in range(9, 0, -1):  
                c = cost[d - 1]
                if t >= c and dp[t - c] != "0":
                    candidate = dp[t - c] + str(d)
                    if dp[t] == "0" or len(candidate) > len(dp[t]) or (len(candidate) == len(dp[t]) and candidate > dp[t]):
                        dp[t] = candidate
        return dp[target] if dp[target] != "0" else "0"
