# 给定两个二叉树，编写一个函数来检验它们是否相同。 
# 
#  如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。 
# 
#  示例 1: 
# 
#  输入:       1         1
#           / \       / \
#          2   3     2   3
# 
#         [1,2,3],   [1,2,3]
# 
# 输出: true 
# 
#  示例 2: 
# 
#  输入:      1          1
#           /           \
#          2             2
# 
#         [1,2],     [1,null,2]
# 
# 输出: false
#  
# 
#  示例 3: 
# 
#  输入:       1         1
#           / \       / \
#          2   1     1   2
# 
#         [1,2,1],   [1,1,2]
# 
# 输出: false
#  
#  Related Topics 树 深度优先搜索 
#  👍 558 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def dfs(p: TreeNode)-> List:
            left = []
            if p:
                stack = [p]
                while stack:
                    tmp = stack.pop()
                    left.append(tmp.val)
                    if tmp.right and tmp.left:
                        stack.append(tmp.right)
                        stack.append(tmp.left)
                    elif tmp.right:
                        stack.append(tmp.right)
                        left.append(None)
                    elif tmp.left:
                        stack.append(tmp.left)
                    else:
                        pass
            return left
        left = dfs(p)
        right = dfs(q)
        # print(left, right)
        return left == right
# leetcode submit region end(Prohibit modification and deletion)
