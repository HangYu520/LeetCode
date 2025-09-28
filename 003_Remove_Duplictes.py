"""
问题: 原地删除已排序数组中的重复元素, 并重排数组, 返回不重复的个数

例:
输入: [1,1,2]

输出: 2, [1,2,_]

条件:
1. 1 <= nums.length <= 3 * 10^4
2. -100 <= nums[i] <= 100
3. nums is sorted in ascending order.
"""

class Solution(object):
    """
    思路: (充分利用数组已排序的特性)
        1. 创建两个指针, 一个指向当前不重复的元素, 一个指向当前遍历的元素
        2. 如果当前元素和前一个元素相同, 则跳过
        3. 否则, 将当前元素复制给当前不重复的元素, 并将当前不重复的元素后移一位
        -- 时间复杂度: O(n), 空间复杂度: O(1)
    """
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [0,0,1,1,1,2,2,3,3,4]
        #  ^ ^
        #  i j
        i, j = 0, 1
        while j < len(nums):
            # 非重复的元素
            if nums[j] != nums[j-1]:
                nums[i+1] = nums[j]
                i += 1
            j += 1
        return i+1

if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(f'nums={nums}')
    k = Solution().removeDuplicates(nums)
    print(f'solution={nums},{k}')