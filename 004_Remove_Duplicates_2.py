"""
问题: 原地删除已排序数组中的重复元素, 重复元素至多出现2次

例:
输入: [1,1,1,2,2,3]

输出: 5, [1,1,2,2,3,_]

条件:
1. 1 <= nums.length <= 3 * 10^4
2. -10^4 <= nums[i] <= 10^4
3. nums is sorted in ascending order.
"""

class Solution(object):
    """
    思路:(如何判断重复2次)
        1. 创建两个指针, 一个指向至多重复2次的元素, 一个指向当前遍历的元素
        2. 如果当前元素和前一个元素不相等, 或与前一个元素相等且重复2次, 则将当前元素加入
        -- 时间复杂度: O(n), 空间复杂度: O(1)
    """
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 3: return n
        # [1,1,1,2,2,3]
        #    ^ ^
        #    i j
        i, j = 1, 2
        
        while j < n:
            # j 和 j-1 不相等 or 相等但重复2次
            if nums[j] != nums[j-1] or nums[j] != nums[i-1]:
                nums[i+1] = nums[j]
                i += 1
            j += 1
        
        return i+1


if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    print(f'nums = {nums}')
    k = Solution().removeDuplicates(nums)
    print(f'solution = {nums[:k]},{k}')