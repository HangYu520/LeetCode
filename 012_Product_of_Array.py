"""
问题: 求数组中每个元素不包含自己的乘积

例:
输入: nums = [1, 2, 3, 4]
输出: [24, 12, 8, 6]

条件:
1. 2 <= nums.length <= 10^5
2. -30 <= nums[i] <= 30
3. 乘积保证不会溢出32位整数
4. 要求时间复杂度O(n), 不使用除法
"""

class Solution(object):
    """
    思路: (多次遍历)
        A. 创建两个数组 lefts 和 rights
        1. lefts 为 nums 中每个元素左边的乘积
        2. rights 为 nums 中每个元素右边的乘积
        3. 返回最终的结果
        -- 时间复杂度: O(n), 空间复杂度: O(n)

        B. 创建一个数组 res 进行空间复用
        1. 计算每个元素左边的乘积存入 res
        2. 单变量更新每个元素右边的乘积, 与左边乘积计算得到最终结果
        -- 时间复杂度: O(n), 空间复杂度: O(1)
    """
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n

        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        rightproduct = 1

        for i in range(n - 2, -1, -1):
            rightproduct *= nums[i + 1]
            res[i] *= rightproduct
        
        return res

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(f'nums = {nums}')
    print(f'solution = {Solution().productExceptSelf(nums)}')