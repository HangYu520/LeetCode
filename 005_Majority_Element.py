"""
问题: 返回数组中出现次数超过一半的多数元素

例:
输入: [3,2,3]
输出: 3

条件:
1. n = nums.length
2. 1 <= n <= 5 * 10^4
3. -10^9 <= nums[i] <= 10^9
"""

class Solution(object):
    """
    思路:
        A. 使用 dict
        1. 利用 dict 存储元素出现的次数
        2. 遍历 dict, 找到出现次数超过一半的元素
        -- 时间复杂度: O(n), 空间复杂度: O(n)

        B. 使用排序
        1. 对数组进行排序
        2. 遍历数组, 找到出现次数超过一半的元素
        -- 时间复杂度: O(nlogn), 空间复杂度: O(1)
        
        C. 使用投票算法
        1. 核心思想：多数元素的出现次数比其他所有元素出现次数之和还要多
        2. 维护一个候选元素(candidate)和计数器(count)
        3. 遍历数组, 如果当前元素等于候选元素, 则计数器加1
        4. 否则, 计数器减1
        5. 如果计数器等于0, 则将候选元素更新为当前元素, 并将计数器置为1
        -- 时间复杂度: O(n), 空间复杂度: O(1)
    """
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate, count = None, 0

        for num in nums:
            if count == 0: 
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate

if __name__ == "__main__":
    nums = [2,2,1,1,1,2,2]
    print(f'nums = {nums}')
    print(f'solution = {Solution().majorityElement(nums)}')