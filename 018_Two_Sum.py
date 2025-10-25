"""
问题: 找到已排序数组中两个数之和为 target 的索引

例:
输入: nums = [2,7,11,15], target = 9
输出: [0,1]

条件:
1. 2 <= nums.length <= 3*10^4
2. -1000 <= nums[i] <= 1000
3. -1000 <= target <= 1000
4. 只会存在一个有效答案
"""

class Solution:
    """
    思路:
        A. 哈希表
        1. 创建一个哈希表，将数组的元素作为键，索引作为值
        2. 遍历数组，将当前元素作为键，索引作为值
        3. 获取目标值，即 target - 当前元素
        -- 时间复杂度: O(n), 空间复杂度: O(n)

        B. 二分法
        1. 遍历数组，将当前元素作为目标值
        2. 使用二分法，在剩余的数组中寻找目标值
        -- 时间复杂度: O(nlogn), 空间复杂度: O(1)

        C. 双指针 (充分利用已排序的特性)
        1. 定义两个指针，分别指向数组的开始和结束
        2. 如果两个指针的值之和等于目标值，返回两个指针的索引
        3. 如果两个指针的值之和小于目标值，移动左指针
        4. 如果两个指针的值之和大于目标值，移动右指针
        -- 时间复杂度: O(n), 空间复杂度: O(1)
    """
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left, right]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1

if __name__ == "__main__":
    nums = [1,2,3,4,4,9,56,90]
    target = 8
    print(f'nums={nums}, target={target}')
    print(f'solution={Solution().twoSum(nums, target)}')