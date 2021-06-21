# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
#
#
#
#  示例 1：
#
#
# 输入：root = [1,null,2,3]
# 输出：[1,2,3]
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
# 输入：root = [1]
# 输出：[1]
#
#
#  示例 4：
#
#
# 输入：root = [1,2]
# 输出：[1,2]
#
#
#  示例 5：
#
#
# 输入：root = [1,null,2]
# 输出：[1,2]
#
#
#
#
#  提示：
#
#
#  树中节点数目在范围 [0, 100] 内
#  -100 <= Node.val <= 100
#
#
#
#
#  进阶：递归算法很简单，你可以通过迭代算法完成吗？
#  Related Topics 栈 树
#  👍 582 👎 0

# 递归
# 思路：根左右
# 时间复杂度：O(N)
# 空间复杂度：O(N)
# 执行耗时:36 ms,击败了84.33% 的Python3用户
# 内存消耗:14.9 MB,击败了16.51% 的Python3用户

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorder(self, root, res):
        if not root:
            return
        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)
    
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.preorder(root, res)
        return res
# leetcode submit region end(Prohibit modification and deletion)
