# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
#
#
#
#  示例：
# 二叉树：[3,9,20,null,null,15,7],
#
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#  返回其层序遍历结果：
#
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#
#  Related Topics 树 广度优先搜索
#  👍 842 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root:
            stack = [root]
            while stack:
                res1 = []
                for _ in range(len(stack)):
                    tmp = stack.pop(0)
                    res1.append(tmp.val)
                    if tmp.left:
                        stack.append(tmp.left)
                    if tmp.right:
                        stack.append(tmp.right)
                res.append(res1)
        return res
        
# leetcode submit region end(Prohibit modification and deletion)
