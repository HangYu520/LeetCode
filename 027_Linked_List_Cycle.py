"""
问题: 判断给定的链表是否有环

例:
输入: head = [3,2,0,-4], pos = 1
输出: true
解释: 链表中有一个环，其尾部连接到第二个节点。

条件:
1. 链表中节点的数目范围在范围 [0, 10^4] 内
2. -10^5 <= Node.val <= 10^5
3. pos 为 -1 或者链表中的一个有效索引
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    思路:
        A. 哈希表
        1. 创建一个哈希表，将所有节点加入表中
        2. 遍历链表, 如果某个节点已经加入表中, 则返回True
        3. 遍历结束, 返回False
        -- 时间复杂度: O(n), 空间复杂度: O(n)
        B. 快慢指针
        1. 创建两个指针, 一个是慢指针, 一个是快指针
        2. 慢指针每次移动一步, 快指针每次移动两步
        3. 如果有环, 快慢指针会相遇
        -- 时间复杂度: O(n), 空间复杂度: O(1)
    """
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    print(f'head = [3,2,0,-4], pos = 1')
    print(Solution().hasCycle(head))