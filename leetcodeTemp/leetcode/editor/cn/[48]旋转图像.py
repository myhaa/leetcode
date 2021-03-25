# date: 2021-03-25 23:10:02

# 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
#
#  你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
#
#
#
#  示例 1：
#
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[7,4,1],[8,5,2],[9,6,3]]
#
#
#  示例 2：
#
#
# 输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# 输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
#
#
#  示例 3：
#
#
# 输入：matrix = [[1]]
# 输出：[[1]]
#
#
#  示例 4：
#
#
# 输入：matrix = [[1,2],[3,4]]
# 输出：[[3,1],[4,2]]
#
#
#
#
#  提示：
#
#
#  matrix.length == n
#  matrix[i].length == n
#  1 <= n <= 20
#  -1000 <= matrix[i][j] <= 1000
#
#  Related Topics 数组
#  👍 835 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 旋转数组，边界问题
# 执行耗时:40 ms,击败了58.78% 的Python3用户
# 内存消耗:14.9 MB,击败了14.28% 的Python3用户
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i0, im, j0, jn = 0, len(matrix)-1, 0, len(matrix)-1
        if i0 == jn:
            return
        while i0 <= jn:
            for i in range(jn-i0):
                tmp = matrix[i0][i0+i]
                matrix[i0][i0+i] = matrix[im-i][j0]
                matrix[im-i][j0] = matrix[im][jn-i]
                matrix[im][jn-i] = matrix[i0+i][jn]
                matrix[i0+i][jn] = tmp
            i0 += 1
            im -= 1
            j0 += 1
            jn -= 1
        return
# leetcode submit region end(Prohibit modification and deletion)
