"""
问题: 给一个数组和目标值，返回满足和>=目标值的最小子数组长度

例:
输入: target = 7, nums = [2,3,1,2,4,3]
输出: 2

条件:
1. 1 <= target <= 10^9
2. 1 <= nums.length <= 10^5
3. 1 <= nums[i] <= 10^4
注 : 子数组的元素必须是连续的
"""

class Solution(object):
    """
    思路:
        A. 动态规划
        1. 创建一个 n*n 的数组dp, dp[i, j]表示 i 开头的长度为 j 子数组和
        2. j 从 1 开始遍历，找到满足和>=目标值的 j 
        -- 时间复杂度: O(n^2), 空间复杂度: O(n)

        B. 滑动窗口 (数组全为正数, 扩大窗口一定增大, 缩小窗口一定减小)
        1. 创建一个滑动窗口，窗口的右边界为 j, 窗口的左边界为 i
        2. 保持窗口的左边界不变时, 不断扩大窗口的右边界
        3. 和>=目标值时, 尝试缩小窗口的左边界, 找到最小的长度
        -- 时间复杂度: O(n), 空间复杂度: O(1)
    """
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n, min_len = len(nums), len(nums) + 1
        left, right, sum = 0, 0, 0

        while right < n:
            sum += nums[right]
            while sum >= target:
                # 缩小窗口
                min_len = min(min_len, right - left + 1)
                sum -= nums[left]
                left += 1
            # 窗口右移
            right += 1
        
        return min_len if min_len <= n else 0

if __name__ == "__main__":
    target = 7
    nums = [2,3,1,2,4,3]
    print(f'target={target}, nums={nums}')
    solution = Solution().minSubArrayLen(target, nums)
    print(f'solution={solution}')