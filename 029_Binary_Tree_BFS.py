"""
问题: 层序遍历二叉树

输入: root = [3,9,20,null,null,15,7]
输出: [[3],[9,20],[15,7]]

条件:
1. 节点个数 [0, 2000]
2. -1000 <= Node.val <= 1000
"""

from binarytree import Node

class Solution(object):
    """
    思路:
        1. 层序遍历二叉树
        2. 创建一个队列，将根节点加入队列
        3. 遍历当前层的节点，将下一层的节点加入队列
        -- 时间复杂度: O(n), 空间复杂度: O(n)
    """
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            tmp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if tmp:
                res.append(tmp)
        return res


if __name__ == "__main__":
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    print(f'root={root}')
    print(f'solution={Solution().levelOrder(root)}')            