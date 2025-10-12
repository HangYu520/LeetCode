"""
问题: 从一个环形加油站的哪一站出发, 才能回到原点

例: 
输入: gas = [1,2,3,4,5], cost = [3,4,5,1,2] (gas 每一个站的油量, cost 去下一站需要消耗的油量)
输出: 3 (从3站出发, 油量足够回到原点, 若任何一站都不可以返回 -1)

条件:
1. n == gas.length == cost.length
2. 1 <= n <= 10^5
3. 0 <= gas[i], cost[i] <= 10^4
4. 如果有答案, 确保一定是唯一的
"""

class Solution(object):
    """
    思路:
        A. 暴力求解
        1. 尝试从每一个站点出发, 模拟加油的过程, 直到油量为0
        2. 若有解, 返回起始站点, 若无解, 返回-1
        -- 时间复杂度: O(n^2), 空间复杂度: O(1)

        B. 单次便历
        关键点: 
        -- 若 A 出发, 在 B 耗尽, 则 AB 中的任何一点都不可能到 B
        -- 若 A 出发能到结尾, 就一定能绕一圈回来 (因为预先检查有解保证)
        -- 所以问题就转为寻找, 从哪一点出发能到结尾?
        
        1. 初始化 current_tank = 0 和 start = 0
        2. 遍历每个站点索引, 更新 current_tank
        3. 若 current_tank < 0, 则无法从 start 出发, 更新 start, 重置
        4. 若遍历结束, 且 current_tank >= 0, 则存在解, 返回 start, 否则返回 -1
        -- 时间复杂度: O(n), 空间复杂度: O(1)
    """
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost): return -1 # 预先检查是否有解

        current_tank, start = 0, 0

        for i in range(len(gas)):
            current_tank += gas[i] - cost[i]
            if current_tank < 0:
                start = i + 1
                current_tank = 0
        
        return start if current_tank >= 0 else -1

if __name__ == "__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print(f'gas = {gas}, cost = {cost}')
    print(f'solution = {Solution().canCompleteCircuit(gas, cost)}')