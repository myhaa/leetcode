# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
#
#  你可以假设除了数字 0 之外，这两个数字都不会以零开头。
#
#
#
#  进阶：
#
#  如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
#
#
#
#  示例：
#
#  输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 8 -> 0 -> 7
#
#  Related Topics 栈 链表 数学
#  👍 403 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        # print(stack1, stack2)
        pre = None
        carry = 0
        while stack1 or stack2 or carry != 0:
            v1 = 0 if not stack1 else stack1.pop()
            v2 = 0 if not stack2 else stack2.pop()
            cur = v1 + v2 + carry
            carry = cur // 10
            cur = cur % 10
            tmp = ListNode(cur)
            tmp.next = pre
            pre = tmp
        return pre
# leetcode submit region end(Prohibit modification and deletion)
