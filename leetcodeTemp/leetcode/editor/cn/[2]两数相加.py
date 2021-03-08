# date: 2021-03-04 22:51:12

# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
#  请你将两个数相加，并以相同形式返回一个表示和的链表。
#
#  你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
#
#
#  示例 1：
#
#
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
#
#
#  示例 2：
#
#
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#
#
#  示例 3：
#
#
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]
#
#
#
#
#  提示：
#
#
#  每个链表中的节点数在范围 [1, 100] 内
#  0 <= Node.val <= 9
#  题目数据保证列表表示的数字不含前导零
#
#  Related Topics 递归 链表 数学
#  👍 5733 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 自己的解法
# 将值放进列表，然后相加，再将列表转成链表
# 时间负责度、空间复杂度都较高
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         # def reverseListNode(l1):
#         #     head = None
#         #     while l1:
#         #         tmp = l1.next
#         #         l1.next = head
#         #         head = l1
#         #         l1 = tmp
#         #     return head
#         # l1 = reverseListNode(l1)
#         # l2 = reverseListNode(l2)
#         # print(l1, l2)
#
#         def ListNodeToList(l1):
#             res = []
#             while l1:
#                 res.append(str(l1.val))
#                 l1 = l1.next
#             return res[::-1]
#
#         l1 = ListNodeToList(l1)
#         l2 = ListNodeToList(l2)
#         # print(l1, l2)
#         res = list(str(int(''.join(l1))+int(''.join(l2))))[::-1]
#         # print(res)
#         head = ListNode(int(res[0]))
#         tmp = head
#         for i in res[1:]:
#             tmp1 = ListNode(int(i))  # 新建一个节点
#             tmp.next = tmp1  # 将head.next指向该节点
#             tmp = tmp1  # 将tmp指向新建节点，此时head节点不会变
#         return head

# 官方解法=
# 时间复杂度：O(MAX(M,N))
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head, tmp, carry = None, None, 0
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            n_sum = n1 + n2 + carry
            if not head:
                tmp = ListNode(n_sum % 10)
                head = tmp
            else:
                tmp.next = ListNode(n_sum % 10)
                tmp = tmp.next
            carry = n_sum // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            tmp.next = ListNode(carry)
        return head

# leetcode submit region end(Prohibit modification and deletion)
