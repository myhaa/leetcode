# 请判断一个链表是否为回文链表。
#
#  示例 1:
#
#  输入: 1->2
# 输出: false
#
#  示例 2:
#
#  输入: 1->2->2->1
# 输出: true
#
#
#  进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
#  Related Topics 链表 双指针
#  👍 867 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        slow.next = None
        while fast:
            tmp = fast.next
            fast.next = slow
            slow = fast
            fast = tmp
        while head and slow:
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next
        return True

# leetcode submit region end(Prohibit modification and deletion)
