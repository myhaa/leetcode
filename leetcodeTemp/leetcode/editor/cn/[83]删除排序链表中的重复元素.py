# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。 
# 
#  示例 1: 
# 
#  输入: 1->1->2
# 输出: 1->2
#  
# 
#  示例 2: 
# 
#  输入: 1->1->2->3->3
# 输出: 1->2->3 
#  Related Topics 链表 
#  👍 458 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tmp= head
        while tmp and tmp.next:
            if tmp.val == tmp.next.val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
            # print(tmp, head)
        return head
# leetcode submit region end(Prohibit modification and deletion)


test = Solution()
print(test.deleteDuplicates(ListNode(1, ListNode(1, ListNode(2, None)))))