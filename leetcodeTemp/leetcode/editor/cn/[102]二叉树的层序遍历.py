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
#  👍 903 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 栈+队列实现二叉树的层序遍历，即广度优先搜索
# 思路
# 时间复杂度：O(N)
# 空间复杂度：O(N)
# 		执行耗时:44 ms,击败了54.24% 的Python3用户
# 		内存消耗:15.2 MB,击败了40.52% 的Python3用户
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            tmp = queue
            queue = []
            res1 = []
            for x in tmp:
                res1.append(x.val)
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
            res.append(res1)
        return res
# leetcode submit region end(Prohibit modification and deletion)
