"""
问题: 给定一个论文引用数组, 求H指数。H指数为至少有h篇论文被引用h次

例:
输入: citations = [3,0,6,1,5]
输出: 3

条件：
1. n == citations.length
2. 1 <= n <= 5000
3. 0 <= citations[i] <= 1000
"""

class Solution(object):
    """
    思路:
        A. 升序排序
        1. 遍历排序后的数组, 找到第一个满足 citations[i] >= n - i 的 i
        2. 返回 n - i
        -- 时间复杂度: O(nlogn), 空间复杂度: O(1)
    """
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        citations.sort()
        for i in range(n):
            if citations[i] >= n - i:
                return n - i
        return 0

if __name__ == '__main__':
    citations = [3,0,6,1,5]
    print(f'citations={citations}')
    print(f'solution={Solution().hIndex(citations)}')