# date: 2021-03-29 19:48:52

# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
#  说明：每次只能向下或者向右移动一步。
#
#
#
#  示例 1：
#
#
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
#
#
#  示例 2：
#
#
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12
#
#
#
#
#  提示：
#
#
#  m == grid.length
#  n == grid[i].length
#  1 <= m, n <= 200
#  0 <= grid[i][j] <= 100
#
#  Related Topics 数组 动态规划
#  👍 827 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 时间复杂度：O(MN)
# 空间复杂度：O(MN)
# 执行耗时:56 ms,击败了61.59% 的Python3用户
# 内存消耗:16.4 MB,击败了22.43% 的Python3用户
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in grid]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[m-1][n-1]
# leetcode submit region end(Prohibit modification and deletion)
