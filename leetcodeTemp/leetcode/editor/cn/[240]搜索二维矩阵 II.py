# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
#
#
#  每行的元素从左到右升序排列。
#  每列的元素从上到下升序排列。
#
#
#
#
#  示例 1：
#
#
# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21
# ,23,26,30]], target = 5
# 输出：true
#
#
#  示例 2：
#
#
# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21
# ,23,26,30]], target = 20
# 输出：false
#
#
#
#
#  提示：
#
#
#  m == matrix.length
#  n == matrix[i].length
#  1 <= n, m <= 300
#  -109 <= matix[i][j] <= 109
#  每行的所有元素从左到右升序排列
#  每列的所有元素从上到下升序排列
#  -109 <= target <= 109
#
#  Related Topics 二分查找 分治算法
#  👍 631 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 从右上角往左往下搜索，利用有序性，等于target，返回true，大于target，向左走，小于target，往下走
# 时间复杂度：O(m+n)
# 空间复杂度：O(1)
# 			执行耗时:204 ms,击败了29.29% 的Python3用户
# 			内存消耗:20.9 MB,击败了71.19% 的Python3用户
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1
        while i < m and j > -1:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
        
# leetcode submit region end(Prohibit modification and deletion)
