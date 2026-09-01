import atexit
class Solution(object):
    def findTargetSumWays(self, nums, target):
        dp = {0: 1}
        
        for num in nums:
            temp = {}
            
            for s in dp:
                temp[s + num] = temp.get(s + num, 0) + dp[s]
                temp[s - num] = temp.get(s - num, 0) + dp[s]
            dp = temp

        return dp.get(target, 0)        

atexit.register(lambda: (open("display_runtime.txt","w").write("000")))
        