"""
问题: 给定股票价格的序列，求购买和售出最大利润

例:
输入: prices = [7,1,5,3,6,4]
输出: 5

条件:
1. 1 <= prices.length <= 10^5
2. 0 <= prices[i] <= 10^4
"""

class Solution(object):
    """
    思路:
        A. 暴力搜索
        1. 遍历所有可能的情况, 找到最大利润
        -- 时间复杂度: O(n^2), 空间复杂度: O(1)

        B. 贪心算法（低买高卖）
        1. 遍历所有价格, 更新最低价格
        2. 遍历所有价格, 更新最大利润
        -- 时间复杂度: O(n), 空间复杂度: O(1)
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price, max_profit = prices[0], 0
        
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i] - min_price)
        
        return max_profit

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(f'prices = {prices}')
    print(f'solution = {Solution().maxProfit(prices)}')