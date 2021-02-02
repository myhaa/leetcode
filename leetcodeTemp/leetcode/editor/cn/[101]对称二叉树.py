# 给定一个二叉树，检查它是否是镜像对称的。 
# 
#  
# 
#  例如，二叉树 [1,2,2,3,4,4,3] 是对称的。 
# 
#      1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#  
# 
#  
# 
#  但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的: 
# 
#      1
#    / \
#   2   2
#    \   \
#    3    3
#  
# 
#  
# 
#  进阶： 
# 
#  你可以运用递归和迭代两种方法解决这个问题吗？ 
#  Related Topics 树 深度优先搜索 广度优先搜索 
#  👍 1222 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# 思路：从前往后遍历，从后往前遍历，然后看是否相等
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         def qianxu1(root: TreeNode):
#             res = []
#             if not root:
#                 return [None]
#             res.append(root.val)
#             return res + qianxu1(root.left) + qianxu1(root.right)
#         def qianxu2(root: TreeNode):
#             res = []
#             if not root:
#                 return [None]
#             res.append(root.val)
#             return res + qianxu2(root.right) + qianxu2(root.left)
#         t1 = qianxu1(root)
#         t2 = qianxu2(root)
#         return t1 == t2

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and check(p.left, q.right) and check(p.right, q.left)
        return check(root, root)
# leetcode submit region end(Prohibit modification and deletion)
