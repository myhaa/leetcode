# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。
#
#
#
#  示例 1：
#
#
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
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
# 输出：[2,1]
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
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#  Related Topics 栈 树 哈希表
#  👍 918 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归
# 执行耗时:44 ms,击败了32.59% 的Python3用户
# 内存消耗:15 MB,击败了8.52% 的Python3用户
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         if root:
#             res.extend(self.inorderTraversal(root.left))
#             res.append(root.val)
#             res.extend(self.inorderTraversal(root.right))
#         return res

# 迭代
# 执行耗时:40 ms,击败了60.24% 的Python3用户
# 内存消耗:14.7 MB,击败了84.25% 的Python3用户
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right
        return res
# leetcode submit region end(Prohibit modification and deletion)
