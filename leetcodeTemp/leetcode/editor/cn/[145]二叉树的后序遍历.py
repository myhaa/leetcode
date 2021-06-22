# 给定一个二叉树，返回它的 后序 遍历。
#
#  示例:
#
#  输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# 输出: [3,2,1]
#
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#  Related Topics 栈 树
#  👍 611 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 递归
# 思路, 左右根
# 时间复杂度：O(N)
# 空间复杂度：O(N)
# 		执行耗时:48 ms,击败了14.68% 的Python3用户
# 		内存消耗:15.1 MB,击败了5.28% 的Python3用户
class Solution:
    def postorder(self, root, res):
        if not root:
            return
        self.postorder(root.left, res)
        self.postorder(root.right, res)
        res.append(root.val)
        
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.postorder(root, res)
        return res


# 栈
# 思路： 前序：根左右， 中序：左根右， 后序：左右根
# 准备两个栈，前序根左右可以弄出来，那根右左是不是可以弄出来，那把根右左反过来就是左右根了
# 时间复杂度：O(N)
# 空间复杂度：O(N)
# 执行耗时:32 ms,击败了95.21% 的Python3用户
# 内存消耗:14.8 MB,击败了53.48% 的Python3用户

# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#
#         if root:
#             stack1 = [root]  # 前序的栈
#             # stack2 = []  # 后序的栈
#             while stack1:
#                 root = stack1.pop()
#                 # stack2.append(root)
#                 res.append(root.val)
#                 if root.left:
#                     stack1.append(root.left)
#                 if root.right:
#                     stack1.append(root.right)
#             # return [i.val for i in stack2[::-1]]
#         return res[::-1]

# leetcode submit region end(Prohibit modification and deletion)
