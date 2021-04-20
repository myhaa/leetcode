# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
#  注意:
# 你可以假设树中没有重复的元素。
#
#  例如，给出
#
#  前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
#
#  返回如下的二叉树：
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  Related Topics 树 深度优先搜索 数组
#  👍 992 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 时间复杂度：O(n)，其中 n 是树中的节点个数。
#
# 空间复杂度：O(n)，除去返回的答案需要的 O(n) 空间之外，我们还需要使用 O(n) 的空间存储哈希映射，以及 O(h)（其中 h 是树的高度）的空间表示递归时栈空间。这里 h < n，所以总空间复杂度为 O(n)。
# 递归
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         def myBuildTrue(preorder_left, preorder_right, inorder_left, inorder_right):
#             if preorder_left > preorder_right:  # 递归终止条件，判断哪些节点应该是在左子树
#                 return
#             preorder_root = preorder_left  # 前序遍历第一个节点就是根节点
#             inorder_root = index[preorder[preorder_root]]  # 在中序遍历中找到根节点所在位置，其左边就是左子树的节点，右边就是右子树的节点
#             root = TreeNode(val=preorder[preorder_root])  # 先记录当前根节点
#             left_size = inorder_root - inorder_left  # 左子树节点的个数
#             root.left = myBuildTrue(preorder_left+1, preorder_left+left_size, inorder_left, inorder_root-1)  # 递归调用左子树
#             root.right = myBuildTrue(preorder_left+left_size+1, preorder_right, inorder_root+1, inorder_right)  # 递归调用右子树
#             return root
#         index = {num : i for i, num in enumerate(inorder)}
#         return myBuildTrue(0, len(preorder)-1, 0, len(inorder)-1)

# 迭代
# 			执行耗时:48 ms,击败了92.84% 的Python3用户
# 			内存消耗:15.6 MB,击败了98.97% 的Python3用户
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        root = TreeNode(val=preorder[0])
        stack = [root]
        index = 0
        for i in range(1, len(preorder)):
            node = stack[-1]
            if stack and node.val != inorder[index]:
                node.left = TreeNode(val=preorder[i])
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[index]:
                    node = stack.pop()
                    index += 1
                node.right = TreeNode(val=preorder[i])
                stack.append(node.right)
        return root
        
# leetcode submit region end(Prohibit modification and deletion)
