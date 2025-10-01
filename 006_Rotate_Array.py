"""
问题: 旋转数组 k 个位置

例:
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: solution = [5,6,7,1,2,3,4]

条件:
1. 1 <= nums.length <= 10^5
2. -2^31 <= nums[i] <= 2^31 - 1
3. 0 <= k <= 10^5
"""

class Solution(object):
    """
    思路: (注意有可能 k > nums.length)
        A. 创建新数组
        1. 从后 k 个元素开始, 逐个将数组中的元素复制到新数组中
        2. 剩余元素从 0 开始复制到新数组中
        -- 时间复杂度: O(n), 空间复杂度: O(n)

        B. 利用 pop 和 insert
        1. 分 k 次 将数组中的元素 pop 出来, 插入到数组的开头
        -- 时间复杂度: O(nk), 空间复杂度: O(1)

        C. 翻转法
        1. 翻转整个数组
        2. 翻转前 k 个元素
        3. 翻转剩余元素
        -- 时间复杂度: O(n), 空间复杂度: O(1)
    """
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n # 处理 k > nums.length 的情况

        def reverse(start, end):
            # 翻转 [start, end] 数组
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    k = 3
    print(f'nums = {nums}, k = {k}')
    Solution().rotate(nums, k)
    print(f'solution = {nums}')