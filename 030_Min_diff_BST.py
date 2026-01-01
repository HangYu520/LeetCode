"""
问题: 找出二叉搜索树中的最小差值

输入: root = [236,104,701,null,227,null,911]
输出: 9

条件:
1. 树中节点的数目范围是 [2, 10^4]
2. 0 <= Node.val <= 10^5
"""

from binarytree import build

class Solution(object):
    """
    思路: 二叉搜索树的特点--中序遍历的结果是一个有序数组
        1. 递归中序遍历二叉树，保存当前的节点值
        2. 不断更新当前节点与前一个节点的差值，并更新最小差值
        3. 已经找到最小差值，提前退出递归
        -- 时间复杂度: O(n), 空间复杂度: O(1)
    """
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.min_diff = float('inf')
        self.pre = None

        def inorder(node):
            if not node: # 空节点
                return
            
            if self.min_diff == 1: # 已经找到最小差值，提前退出递归
                return
           
            inorder(node.left)
            
            if self.pre: # 跳过第一个节点
                self.min_diff = min(self.min_diff, node.val - self.pre.val)
            
            self.pre = node # 更新前一个节点
            
            inorder(node.right)
        
        inorder(root)

        return self.min_diff

if __name__ == "__main__":
    root = build([236,104,701,None,227,None,911])
    print(f'root={root}')
    print(f'solution={Solution().getMinimumDifference(root)}')