"""
问题: 给定一个二维数组matrix, 将matrix顺时针旋转90度

例:
输入:
 [[1,2,3],
  [4,5,6],
  [7,8,9]]
输出:
 [[7,4,1],
  [8,5,2],
  [9,6,3]]

条件:
1. n == matrix.length == matrix[i].length
2. 1 <= n <= 20
3. -1000 <= matrix[i][j] <= 1000
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for i in range(n):
            # 先转置
            for j in range(i, n):
                t = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = t
            # 再翻转
            left, right = 0, n-1
            while left < right:
                t = matrix[i][left]
                matrix[i][left]  = matrix[i][right]
                matrix[i][right] = t
                left += 1
                right -= 1

if __name__ == "__main__":
    matrix = \
    [
     [1,2,3],
     [4,5,6],
     [7,8,9]
    ]
    print(matrix)
    Solution().rotate(matrix)
    print(matrix)