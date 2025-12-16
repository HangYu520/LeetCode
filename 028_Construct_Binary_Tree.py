"""
问题: 从前序和中序遍历构建二叉树

例:
输入 : preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出 : [3,9,20,null,null,15,7]

条件:
1. preorder.length == inorder.length
2. 1 <= preorder.length <= 3000
3. -3000 <= preorder[i], inorder[i] <= 3000
4. preorder 和 inorder 均 无重复 元素
"""

from binarytree import Node

class Solution(object):
    """
    思路: # ! 注意遍历的元素不存在重复值
        递归, 关键在于确定根节点, 递归调用左右子树
        1. 根据前序遍历确定根节点: 根节点是前序遍历的第一个元素
        2. 根据中序遍历确定左右子树: 左、右子树: 中序遍历的索引范围是根节点索引的左、右边
        3. 构建哈希表来避免查找中序遍历的元素
        -- 时间复杂度: O(n), 空间复杂度: O(n)
    """
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def build(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None
            
            root_val = preorder[preorder_left]
            root = Node(root_val)

            root_idx = inorder_map[root_val]
            left_size = root_idx - inorder_left

            root.left = build(
                preorder_left + 1, 
                preorder_left + left_size, 
                inorder_left, 
                root_idx - 1
            )

            root.right = build(
                preorder_left + left_size + 1, 
                preorder_right, 
                root_idx + 1, 
                inorder_right
            )
            
            return root
        
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    print(f"preorder: {preorder}, inorder: {inorder}")
    print(Solution().buildTree(preorder, inorder))