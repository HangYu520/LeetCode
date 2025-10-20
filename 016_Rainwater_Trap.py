"""
问题: 给直方图表示的柱子高度数组，计算下雨后能接多少雨水

例:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6 (见[图](rainwatertrap.png))

条件:
1. 1 <= height.length <= 2 * 10^4
2. 0 <= height[i] <= 10^5
"""

class Solution(object):
    """
    思路:
        双指针法 (核心逻辑: 谁矮谁先算)
        1. 两个人从两边向中间走, 每人手里拿着一把尺子, 记录自己走过的最高柱子高度(left_max 和 right_max)
        2. 左边人(left)发现当前柱子比右边人(right)的柱子矮说, 明左边的水位由左边最高柱子决定（因为右边有更高的柱子兜底，水不会从右边漏掉）
        3. 右边人(right)发现当前柱子比左边人(left)的柱子矮说, 明右边的水位由右边最高柱子决定（因为左边有更高的柱子兜底，水不会从左边漏掉）
        -- 时间复杂度: O(n), 空间复杂度: O(1)
    """
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water_trapped = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water_trapped += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water_trapped += right_max - height[right]
                right -= 1
        return water_trapped

if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(f'height = {height}')
    print(f'solution = {Solution().trap(height)}')