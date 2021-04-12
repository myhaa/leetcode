# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
#
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#
#
#  示例 1：
#
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "AB
# CCED"
# 输出：true
#
#
#  示例 2：
#
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SE
# E"
# 输出：true
#
#
#  示例 3：
#
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "AB
# CB"
# 输出：false
#
#
#
#
#  提示：
#
#
#  m == board.length
#  n = board[i].length
#  1 <= m, n <= 6
#  1 <= word.length <= 15
#  board 和 word 仅由大小写英文字母组成
#
#
#
#
#  进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？
#  Related Topics 数组 回溯算法
#  👍 863 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 回溯
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            flag.append((i, j))
            for x, y in directions:
                new_i, new_j = i+x, j+y
                if 0<=new_i<row and 0<=new_j<col and (new_i, new_j) not in flag and backtrack(new_i, new_j, k+1):
                    return True
            flag.pop()
            return False
        
        row, col = len(board), len(board[0])
        flag = list()
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        for i in range(row):
            for j in range(col):
                if backtrack(i, j, 0):
                    return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
