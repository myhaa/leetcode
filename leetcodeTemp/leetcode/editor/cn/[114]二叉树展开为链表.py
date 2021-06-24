# 给你二叉树的根结点 root ，请你将它展开为一个单链表：
#
#
#  展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
#  展开后的单链表应该与二叉树 先序遍历 顺序相同。
#
#
#
#
#  示例 1：
#
#
# 输入：root = [1,2,5,3,4,null,6]
# 输出：[1,null,2,null,3,null,4,null,5,null,6]
#
#
#  示例 2：
#
#
# 输入：root = []
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：root = [0]
# 输出：[0]
#
#
#
#
#  提示：
#
#
#  树中结点数在范围 [0, 2000] 内
#  -100 <= Node.val <= 100
#
#
#
#
#  进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？
#  Related Topics 栈 树 深度优先搜索 链表 Binary Tree
#  👍 828 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 栈
# 思路： 结合二叉树的先序遍历，递归实现
# 然后遍历先序遍历结果，实现原地修改结构为链表
# 时间复杂度：O(N)
# 空间复杂度：O(N)
# 		执行耗时:48 ms,击败了46.49% 的Python3用户
# 		内存消耗:15.3 MB,击败了5.09% 的Python3用户
# class Solution:
#     def preorder(self, root, res):
#         if not root:
#             return
#         res.append(root.val)
#         self.preorder(root.left, res)
#         self.preorder(root.right, res)
#
#     def flatten(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         res = []
#         self.preorder(root, res)
#         x = root
#         for i in res[1:]:
#             x.left = None
#             x.right = TreeNode(i)
#             x = x.right
#         # print(res)


# 实现O(1)空间复杂度
# 时间复杂度：O(N)
# 空间复杂度：O(1)
# 		执行耗时:32 ms,击败了98.59% 的Python3用户
# 		内存消耗:14.8 MB,击败了92.03% 的Python3用户
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            if cur.left:
                pre = nxt = cur.left
                while pre.right:
                    pre = pre.right
                pre.right = cur.right
                cur.left = None
                cur.right = nxt
            cur = cur.right
            
# leetcode submit region end(Prohibit modification and deletion)
