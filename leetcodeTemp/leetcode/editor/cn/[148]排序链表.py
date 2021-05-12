# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
#
#  进阶：
#
#
#  你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
#
#
#
#
#  示例 1：
#
#
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
#
#
#  示例 2：
#
#
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
#
#
#  示例 3：
#
#
# 输入：head = []
# 输出：[]
#
#
#
#
#  提示：
#
#
#  链表中节点的数目在范围 [0, 5 * 104] 内
#  -105 <= Node.val <= 105
#
#  Related Topics 排序 链表
#  👍 1111 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 利用辅助数组，记录链表值，然后利用python已有函数排序
# 再重构链表
# 时间复杂度：O(NlogN)
# 空间复杂度：O(N)
# 			执行耗时:244 ms,击败了90.04% 的Python3用户
# 			内存消耗:37.4 MB,击败了8.00% 的Python3用户
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        # print(res)
        res.sort()
        tmp = ListNode()
        res1 = tmp
        for i in res:
            res1.next = ListNode(i)
            res1 = res1.next
        return tmp.next
# leetcode submit region end(Prohibit modification and deletion)
