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
# 利用线性表存储链表顺序，然后通过线性表下标来重排
# 时间复杂度：O(N)
# 空间复杂度：O(N)
# 		执行耗时:140 ms,击败了5.25% 的Python3用户
# 		内存消耗:22.8 MB,击败了96.35% 的Python3用户
# class Solution:
#     def reorderList(self, head: ListNode) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         if not head:
#             return
#         tmp = []
#         root = head
#         while root:
#             tmp.append(root.val)
#             root = root.next
#         flag = True
#         stack = []
#         p, q = 0, len(tmp)-1
#         while p <= q:
#             if flag:
#                 stack.append(tmp[p])
#                 p += 1
#                 flag = False
#             else:
#                 stack.append(tmp[q])
#                 q -= 1
#                 flag = True
#         for i in stack[1:]:
#             head.next = ListNode(i)
#             head = head.next


# 链表中点+反转链表+合并链表
# 思路：
# 重排链表的结果为链表前半段和后半段反转的合并结果
# 找链表中点，通过快慢指针
# 反转链表，通过迭代法
# 合并链表，直接合并
# 时间复杂度：O(N)
# 空间复杂度：O(1)
# 		执行耗时:92 ms,击败了41.91% 的Python3用户
# 		内存消耗:23.1 MB,击败了14.58% 的Python3用户
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        middle_node = self.func_find_middle(head)
        l1 = head  # 左半部分
        l2 = middle_node.next  # 右半部分
        middle_node.next = None  # 这里会实现l1是真正的左半部分
        l2 = self.func_inverse_list_node(l2)  # 将右半部分反转
        # print(l1, l2)
        self.func_merge_l1_l2(l1, l2)  # 合并左半部分，右半部分
    
    def func_find_middle(self, head):
        """
        找出链表中点：快慢指针
        :param head:
        :return:
        """
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def func_inverse_list_node(self, head):
        """
        反转链表：迭代
        :param head:
        :return:
        """
        prev = None  # 设置一个前置节点
        while head:
            tmp = head.next  # 记住下一个节点
            head.next = prev  # 然后将指针跳转方向
            prev = head  # 前置节点指向跳转后的节点
            head = tmp  # 头结点在往后移一个
        return prev
    
    def func_merge_l1_l2(self, l1, l2):
        """
        合并中左，中右
        :param l1:
        :param l2:
        :return:
        """
        while l1 and l2:
            l1_tmp, l2_tmp = l1.next, l2.next
            
            l1.next = l2
            l1 = l1_tmp
            
            l2.next = l1
            l2 = l2_tmp
        
# leetcode submit region end(Prohibit modification and deletion)
