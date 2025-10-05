"""
问题: 数组每个元素代表可以跳跃的最大长度, 判断是否能够到达最后一个位置

例:
输入: [2,3,1,1,4]
输出: true

条件:
1. 1 < nums.length <= 10^4
2. 0 < nums[i] < 10^5
"""

class Solution(object):
    """
    思路: (贪心算法)
        1. 维护一个变量记录当前能到达的最远位置
        2. 遍历数组, 遇到一个位置 i, 如果 i > max_index, 则返回 False
        3. 否则, 更新 max_index 为 max(max_index, i + nums[i])
        -- 时间复杂度: O(n), 空间复杂度: O(1)
    """
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_index = 0
        for i in range(len(nums)):
            if i > max_index:
                return False
            max_index = max(max_index, i + nums[i])
        return True

if __name__ == '__main__':
    nums = [2,3,1,1,4]
    print(f'nums = {nums}')
    print(Solution().canJump(nums))