"""
问题: 计算生命游戏的下一状态

根据「生命游戏」的规则,给定一个包含 m x n 个格子的面板 board ,每个格子可以是活细胞(1)或死细胞(0)。每个格子与其八个相邻格子(水平、垂直、对角线)共同决定下一个状态。下一个状态由以下规则决定：

1. 如果活细胞周围八个位置的活细胞数少于两个,则该位置活细胞死亡(即变为0),模拟“人口过少”。
2. 如果活细胞周围八个位置有两个或三个活细胞,则该位置活细胞仍然存活。
3. 如果活细胞周围八个位置有超过三个活细胞,则该位置活细胞死亡(即变为0),模拟“人口过多”。
4. 如果死细胞周围正好有三个活细胞,则该位置死细胞复活(即变为1),模拟 “繁殖”。

例：
输入: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
输出: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

条件:
1. m == board.length
2. n == board[i].length
3. 1 <= m, n <= 25
4. board[i][j] is 0 or 1.
"""

class Solution(object):
    """
    思路: 使用状态标记法 + 原地修改
        1. 遍历面板每个格子周边八个位置,统计活细胞数量
        2. 为了不引入额外空间,使用状态标记法:
            - 0: 死细胞 -> 死细胞
            - 1: 活细胞 -> 活细胞
            - 2: 活细胞 -> 死细胞
            - 3: 死细胞 -> 活细胞
        -- 时间复杂度: O(m*n), 空间复杂度: O(1)
    """
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])
        
        # 第一遍遍历：标记状态变化
        for i in range(m):
            for j in range(n):
                live_count = 0
                for x in range(max(0, i-1), min(m, i+2)):
                    for y in range(max(0, j-1), min(n, j+2)):
                        if (x != i or y != j) and board[x][y] in (1, 2):
                            live_count += 1
                
                if board[i][j] == 1 and (live_count < 2 or live_count > 3):
                    board[i][j] = 2  # 活细胞将死亡
                elif board[i][j] == 0 and live_count == 3:
                    board[i][j] = 3  # 死细胞将复活
        
        # 第二遍遍历：应用状态变化
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1

if __name__ == "__main__":
    board = \
    [[1, 1],
     [1, 0]]
    print(f"Original board:{board}")
    Solution().gameOfLife(board)
    print(f"Next state board:{board}")