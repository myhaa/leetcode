# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
#
#  你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#  示例 1:
#
#  给定链表 1->2->3->4, 重新排列为 1->4->2->3.
#
#  示例 2:
#
#  给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
#  Related Topics 栈 递归 链表 双指针
#  👍 604 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 栈
# 思路
# 时间复杂度
# 空间复杂度
# 		执行耗时:140 ms,击败了5.25% 的Python3用户
# 		内存消耗:22.8 MB,击败了96.35% 的Python3用户
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        tmp = []
        root = head
        while root:
            tmp.append(root.val)
            root = root.next
        flag = True
        stack = []
        p, q = 0, len(tmp)-1
        while p <= q:
            if flag:
                stack.append(tmp[p])
                p += 1
                flag = False
            else:
                stack.append(tmp[q])
                q -= 1
                flag = True
        for i in stack[1:]:
            head.next = ListNode(i)
            head = head.next
# leetcode submit region end(Prohibit modification and deletion)
