# date: 2021-03-16 23:51:34

# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
#
#
#  示例 1：
#
#
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
#
#
#  示例 2：
#
#
# 输入：l1 = [], l2 = []
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：l1 = [], l2 = [0]
# 输出：[0]
#
#
#
#
#  提示：
#
#
#  两个链表的节点数目范围是 [0, 50]
#  -100 <= Node.val <= 100
#  l1 和 l2 均按 非递减顺序 排列
#
#  Related Topics 递归 链表
#  👍 1600 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 递归
# 			执行耗时:44 ms,击败了66.05% 的Python3用户
# 			内存消耗:14.9 MB,击败了25.18% 的Python3用户
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         if not l1:
#             return l2
#         if not l2:
#             return l1
#         if l1.val < l2.val:
#             l1.next = self.mergeTwoLists(l1.next, l2)
#             return l1
#         else:
#             l2.next = self.mergeTwoLists(l1, l2.next)
#             return l2

# 迭代
# 			执行耗时:40 ms,击败了85.94% 的Python3用户
# 			内存消耗:14.7 MB,击败了84.14% 的Python3用户
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(-1)
        prev = res
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if l1 else l2
        return res.next
# leetcode submit region end(Prohibit modification and deletion)
