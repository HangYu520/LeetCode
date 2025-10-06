"""
问题: 数组元素代表可以跳跃的最大长度, 计算到达最末所需最少跳跃次数

例: 
输入: [2,3,1,1,4]
输出: 2

条件:
1. 1 <= nums.length <= 10^4
2. 0 <= nums[i] <= 1000
3. 确保一定可以到达末尾
"""

class Solution(object):
    """
    思路: (主要是跳的远的同时保证跳的次数少)
        A. 贪心算法 + BFS
        1. jumps : 当前跳跃次数
        2. cur_end : 当前跳跃的最远距离
        3. farthest : [当前, cur_end]中所有可达的最远距离
        -- 时间复杂度: O(n), 空间复杂度: O(1)
    """
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps, cur_end, farthest = 0, 0, 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            
            if i == cur_end:
                jumps += 1
                cur_end = farthest
            
            if cur_end >= len(nums) - 1:
                break
        
        return jumps

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print(f'nums = {nums}')
    print(f'solution = {Solution().jump(nums)}')