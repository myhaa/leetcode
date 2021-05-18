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
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         m, n = len(matrix), len(matrix[0])
#         i, j = 0, n-1
#         while i < m and j > -1:
#             if matrix[i][j] == target:
#                 return True
#             elif matrix[i][j] > target:
#                 j -= 1
#             else:
#                 i += 1
#         return False


# 二分查找
# * 时间复杂度：*O(lg(n!))*。
# * 空间复杂度：*O(1)*，因为我们的二分搜索实现并没有真正地切掉矩阵中的行和列的副本，我们可以避免分配大于常量内存。
# 			执行耗时:168 ms,击败了98.39% 的Python3用户
# 			内存消耗:21 MB,击败了22.50% 的Python3用户
class Solution:
    def binarySearch(self, matrix, target, start, vertical):
        lo = start
        hi = len(matrix) - 1
        if vertical:
            hi = len(matrix[0]) - 1
        while lo <= hi:
            mid = (lo+hi) >> 1
            if vertical:
                if matrix[start][mid] == target:
                    return True
                elif matrix[start][mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                if matrix[mid][start] == target:
                    return True
                elif matrix[mid][start] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(min(len(matrix), len(matrix[0]))):
            x1 = self.binarySearch(matrix, target, i, False)
            x2 = self.binarySearch(matrix, target, i, True)
            if x1 or x2:
                return True
        return False

# leetcode submit region end(Prohibit modification and deletion)
