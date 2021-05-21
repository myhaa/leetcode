# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
#
#
#
#  示例 1：
#
#
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"]
# ,["1","0","0","1","0"]]
# 输出：4
#
#
#  示例 2：
#
#
# 输入：matrix = [["0","1"],["1","0"]]
# 输出：1
#
#
#  示例 3：
#
#
# 输入：matrix = [["0"]]
# 输出：0
#
#
#
#
#  提示：
#
#
#  m == matrix.length
#  n == matrix[i].length
#  1 <= m, n <= 300
#  matrix[i][j] 为 '0' 或 '1'
#
#  Related Topics 动态规划
#  👍 765 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 暴力解法
# 时间复杂度：![O(mn\min(m,n)^2) ] ，其中 *m* 和 *n* 是矩阵的行数和列数。
#    * 需要遍历整个矩阵寻找每个 *1*，遍历矩阵的时间复杂度是 *O(mn)*。
#    * 对于每个可能的正方形，其边长不超过 *m* 和 *n* 中的最小值，需要遍历该正方形中的每个元素判断是不是只包含 *1*，遍历正方形时间复杂度是 ![O(\min(m,n)^2) ]
#    * 总时间复杂度是 ![O(mn\min(m,n)^2) ](./p__O_mn_min_m,n_^2__.png) 。
#
# * 空间复杂度：*O(1)*。额外使用的空间复杂度为常数。
# 			执行耗时:900 ms,击败了5.00% 的Python3用户
# 			内存消耗:20.3 MB,击败了59.74% 的Python3用户
# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         if len(matrix) == 0 or len(matrix[0]) == 0:  # 先判断数组是否空
#             return 0
#         row, col = len(matrix), len(matrix[0])  # 行列
#         max_side = 0  # 边长
#         for i in range(row):  # 遍历
#             for j in range(col):
#                 if matrix[i][j] == '1':  # 找到不为1的点，作为正方形的左点
#                     max_side = max(max_side, 1)  # 更新边长
#                     currentMaxSide = min(row-i, col-j)  # 剩下能够遍历的长度
#                     for k in range(1, currentMaxSide):  # 遍历
#                         flag = True  # flag
#                         if matrix[i+k][j+k] == '0':  # 如果右下点是0，则直接break
#                             break
#                         for x in range(k):  # 遍历
#                             if matrix[i+k][j+x] == '0' or matrix[i+x][j+k] == '0':  # 往右或往下是0，则break
#                                 flag = False
#                                 break
#                         if flag:  # 如果flag是true，则更新边长
#                             max_side = max(max_side, k+1)
#                         else:
#                             break  # 否则break
#         return max_side*max_side

# 动态规划
# 状态转移方程为：dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
# 时间复杂度：O(MN)
# 空间复杂度：O(MN)
# 			执行耗时:116 ms,击败了26.76% 的Python3用户
# 			内存消耗:20.2 MB,击败了78.38% 的Python3用户
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:  # 先判断数组是否空
            return 0
        row, col = len(matrix), len(matrix[0])  # 行列
        dp = [[0]*col for _ in range(row)]
        max_side = 0  # 边长
        for i in range(row):  # 遍历
            for j in range(col):
                if matrix[i][j] == '1':  # 找到不为1的点，作为正方形的左点
                    dp[i][j] = 1 if i == 0 or j == 0 else min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                    max_side = max(dp[i][j], max_side)
                
        return max_side*max_side
# leetcode submit region end(Prohibit modification and deletion)
