# date: 2021-04-24 16:14:45

# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
#  为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，po
# s 仅仅是用于标识环的情况，并不会作为参数传递到函数中。
#
#  说明：不允许修改给定的链表。
#
#  进阶：
#
#
#  你是否可以使用 O(1) 空间解决此题？
#
#
#
#
#  示例 1：
#
#
#
#
# 输入：head = [3,2,0,-4], pos = 1
# 输出：返回索引为 1 的链表节点
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
#
#  示例 2：
#
#
#
#
# 输入：head = [1,2], pos = 0
# 输出：返回索引为 0 的链表节点
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
#
#  示例 3：
#
#
#
#
# 输入：head = [1], pos = -1
# 输出：返回 null
# 解释：链表中没有环。
#
#
#
#
#  提示：
#
#
#  链表中节点的数目范围在范围 [0, 104] 内
#  -105 <= Node.val <= 105
#  pos 的值为 -1 或者链表中的一个有效索引
#
#  Related Topics 链表 双指针
#  👍 973 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 借助哈希表，遍历链表，如果出现重复值则说明有环，
# 时间复杂度：O(N)
# 空间复杂度：O(N)
# 			执行耗时:984 ms,击败了5.37% 的Python3用户
# 			内存消耗:17.9 MB,击败了24.28% 的Python3用户
# class Solution:
#     def detectCycle(self, head: ListNode) -> ListNode:
#         visited = []
#         while head:
#             if head in visited:
#                 return head
#             visited.append(head)
#             head = head.next
#         return None


# 借助快慢指针
# 时间复杂度：O(N)
# 空间复杂度：O(1)
# 			执行耗时:60 ms,击败了65.93% 的Python3用户
# 			内存消耗:17.8 MB,击败了85.48% 的Python3用户
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while fast:
            if not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                tmp = head
                while slow != tmp:
                    slow = slow.next
                    tmp = tmp.next
                return tmp
        return None

# leetcode submit region end(Prohibit modification and deletion)
