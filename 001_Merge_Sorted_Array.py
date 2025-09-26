"""
问题： 给定两个有序的整数数组，合并两个数组，要求合并后的数组依然有序。

例：
输入：
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6], n = 3

输出：
nums1 = [1,2,2,3,5,6]

条件：
1. nums1 的长度为 m + n
2. nums2 的长度为 n
3. 0<= m, n <= 200
4. 1<= m+n <= 200
5. -10^9 <= nums1[i], nums2[i] <= 10^9
"""

class Solution(object):
    """
    思路： 

        1. 创建一个新数组, 前向双指针比较两个数组的元素, 将较小的元素加入新数组中
        -- 时间复杂度: O(m+n), 空间复杂度: O(m+n)
        -- 缺点: 需要创建一个新数组, 无法实现原地修改

        2. 逆向双指针（从后往前合并）
        -- 时间复杂度: O(m+n), 空间复杂度: O(1)
        -- 优点: 原地修改, 将较大的元素移动到新数组的末尾, 直接覆盖
    
    """
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # nums1 = [1,2,3,0,0,0]
        #              ^     ^
        #              i     p
        #
        # nums2 = [2,5,6]
        #              ^
        #              j
        i, j, p = m-1, n-1, m+n-1

        while j > -1:
            # i 没遍历完 且 nums1[i] > nums2[j]
            if i > -1 and nums1[i] > nums2[j]:
                nums1[p] = nums1[i]
                i -= 1 # i 前移
            # i 遍历完 或 nums1[i] < nums2[j]
            else:
                nums1[p] = nums2[j] # j 去 p
                j -= 1 # j 前移
            
            p -= 1 # 固定前移 p


if __name__ == '__main__':
    nums1 = [4,0,0,0,0,0]
    m = 1
    nums2 = [1,2,3,5,6]
    n = 5
    print(f'nums1 = {nums1}')
    print(f'nums2 = {nums2}')
    Solution().merge(nums1, m, nums2, n)
    print(f'solution = {nums1}')