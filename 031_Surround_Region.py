"""
问题: 寻找图中被包围的区域

描述：
给定一个二维的矩阵，包含'X'和'O'，将所有被'X'包围的'O'变成'X'。
每个格子与水平和垂直的格子相连。只有当所有相连的格子全是 'X' 时（不包括边界），该格子才被包围。

例：
输入:
X X X X
X O O X
X X O X
X O X X

输出:
X X X X
X X X X
X X X X
X O X X

条件:
1. m == board.length
2. n == board[i].length
3. 1 <= m, n <= 200
4. board[i][j] is 'X' or 'O'.
"""

from collections import deque

class Solution(object):
    """
    思路: 如何寻找连通区域, 并判断是否被包围
        1. 对于每个格子, 需要利用图的 DFS 或者 BFS 来寻找连通的区域
        2. 与此同时，使用一个 visited 数组来记录已经访问过的格子
        3. 第一种思路: 逐一访问每个 'O' 格子，并判断与之相连的区域是否被包围
        3. 第二种思路: 逐一访问每个边界上的 'O' 格子, 并修改与之不相连的 'O' 格子
        -- 显然第二种思路可以减少很多不必要的遍历, 效率更高
        -- 时间复杂度: O(m * n), 空间复杂度: O(m * n)
    """
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(i, j):
            queue = deque([(i, j)])
            while queue:
                (x, y) = queue.popleft()
                board[x][y] = '*' # 标记为已访问
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                        queue.append((nx, ny))
        
        def dfs(i, j):
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != 'O':
                return
            board[i][j] = '*'
            for dx, dy in directions:
                dfs(i + dx, j + dy)
        
        # 第一次遍历: 丛边界出发寻找连通区域
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)
        
        # 第二次遍历: 修改与边界不相连的 'O' 格子
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X' # 修改为 'X'
                elif board[i][j] == '*':
                    board[i][j] = 'O' # 恢复为 'O'

if __name__ == "__main__":
    board = \
    [["X","X","X","X"],
     ["X","O","O","X"],
     ["X","X","O","X"],
     ["X","O","X","X"]]
    print(f'board={board}')
    Solution().solve(board)
    print(f'solution={board}')