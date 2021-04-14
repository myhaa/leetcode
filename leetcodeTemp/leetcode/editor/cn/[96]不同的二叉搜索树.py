# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
#
#  示例:
#
#  输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#  Related Topics 树 动态规划
#  👍 1121 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 动态规划
# 有序序列，每个点作为根节点，以这个点一分为二，左边放左子树，右边放右子树，构成二叉搜索树，
# 然后形成2个子问题，又复用，所以可以动态规划
# 执行耗时:44 ms,击败了29.53% 的Python3用户
# 内存消耗:14.8 MB,击败了50.48% 的Python3用户
class Solution:
    def numTrees(self, n: int) -> int:
        res = [0] * (n+1)
        res[0] = 1
        res[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                res[i] += res[j-1] * res[i-j]
        return res[-1]
# leetcode submit region end(Prohibit modification and deletion)
