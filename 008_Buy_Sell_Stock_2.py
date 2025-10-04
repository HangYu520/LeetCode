"""
问题: 给定股票价格的序列，求购买和售出最大利润, 可以多次买卖

例:
输入: prices = [7,1,5,3,6,4]
输出: 7

条件:
1. 1 <= prices.length <= 3*10^4
2. 0 <= prices[i] <= 10^4
"""

class Solution(object):
    """
    思路:(允许多次买卖, 低买高卖失效)
        1. 动态规划, dp[i][0] 表示第i天不持有股票时的最大利润, dp[i][1] 表示第i天持有股票时的最大利润
        2. 状态转移方程:
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        3. 初始条件:
            dp[0][0] = 0
            dp[0][1] = -prices[0]
        -- 时间复杂度: O(n), 空间复杂度: O(n)
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]
        # 初始条件
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        # 状态转移方程
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        
        return dp[-1][0]

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(f'prices = {prices}')
    print(f'solution = {Solution().maxProfit(prices)}')