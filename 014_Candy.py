"""
问题: 为每个小孩分发糖果所需的最小的糖果数

例:
输入: ratings = [1,0,2] (每个小孩有一个得分)
输出: 5 (分发糖果数2, 1, 2, 要求每个小孩至少有一个糖果, 且比相邻评分高的小孩获得更多的糖果)

条件:
1. n == ratings.length
2. 1 <= n <= 2 * 10^4
3. 0 <= ratings[i] <= 2 * 10^4
"""

class Solution(object):
    """
    思路:
       A. 两次遍历
       1. 初始化糖果数组为全1, 保证每个小孩至少有一个糖果
       2. 从左到右遍历, 确保满足右边约束
       3. 从右到左遍历, 确保满足左边约束
       4. 返回糖果数组的和
       -- 时间复杂度: O(n), 空间复杂度: O(n)
    """
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candy = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candy[i] = max(candy[i], candy[i+1] + 1)
        
        return sum(candy)

if __name__ == "__main__":
    nums = [1,0,2]
    print(f'nums = {nums}')
    print(f'solution = {Solution().candy(nums)}')