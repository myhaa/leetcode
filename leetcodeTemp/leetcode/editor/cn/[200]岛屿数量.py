# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
#  岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
#
#  此外，你可以假设该网格的四条边均被水包围。
#
#
#
#  示例 1：
#
#
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
#
#
#  示例 2：
#
#
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
#
#
#
#
#  提示：
#
#
#  m == grid.length
#  n == grid[i].length
#  1 <= m, n <= 300
#  grid[i][j] 的值为 '0' 或 '1'
#
#  Related Topics 深度优先搜索 广度优先搜索 并查集
#  👍 1147 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 深度优先遍历
# 遇到1，开始深度优先，岛屿+1，将上下，左右遇到的1变为0，代表这片区域是岛屿
# 时间复杂度：O(MN)
# 空间复杂度：O(MN)
# 			执行耗时:88 ms,击败了38.35% 的Python3用户
# 			内存消耗:18.7 MB,击败了56.89% 的Python3用户
class Solution:
    def dfs(self, grid, r, c):
        grid[r][c] = '0'
        nr, nc = len(grid), len(grid[0])
        for x, y in ([r-1, c], [r, c-1], [r+1, c], [r, c+1]):
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == '1':
                self.dfs(grid, x, y)
    
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        island = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':
                    island += 1
                    self.dfs(grid, i, j)
        return island
# leetcode submit region end(Prohibit modification and deletion)
