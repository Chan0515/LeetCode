class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1]*(amount + 1)
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i+coin<=len(dp)-1:
                    dp[i + coin] = min(dp[i + coin],dp[i] + 1)
        return dp[-1] if dp[-1]<=amount else -1