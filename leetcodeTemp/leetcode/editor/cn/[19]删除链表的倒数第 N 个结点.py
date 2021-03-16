# date: 2021-03-16 22:40:21

# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
#
#  进阶：你能尝试使用一趟扫描实现吗？
#
#
#
#  示例 1：
#
#
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
#
#
#  示例 2：
#
#
# 输入：head = [1], n = 1
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：head = [1,2], n = 1
# 输出：[1]
#
#
#
#
#  提示：
#
#
#  链表中结点的数目为 sz
#  1 <= sz <= 30
#  0 <= Node.val <= 100
#  1 <= n <= sz
#
#  Related Topics 链表 双指针
#  👍 1274 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 双指针
# 时间复杂度：O(N)
# 空间复杂度：O(1)
# 执行耗时:44 ms,击败了50.13% 的Python3用户
# 内存消耗:14.8 MB,击败了60.13% 的Python3用户
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or not head.next:
            return
        res = ListNode(0, head)
        p, q = res, head
        for i in range(n):
            q = q.next
        while q:
            q = q.next
            p = p.next
        p.next = p.next.next
        return res.next
# leetcode submit region end(Prohibit modification and deletion)
