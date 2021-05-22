# date: 2021-05-22 17:32:32

# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
#
#  给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。
#
#  完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
#
#
#
#
#  示例 1：
#
#
# 输入：n = 12
# 输出：3
# 解释：12 = 4 + 4 + 4
#
#  示例 2：
#
#
# 输入：n = 13
# 输出：2
# 解释：13 = 4 + 9
#
#
#  提示：
#
#
#  1 <= n <= 104
#
#  Related Topics 广度优先搜索 数学 动态规划
#  👍 875 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

# 暴力解法
# minnum(n) = min(minnum(n-k)+1)  对任意完全平方数K
# 时间复杂度：O()
# 			Time Limit Exceeded
import math
class Solution:
    def numSquares(self, n: int) -> int:
        squareList = [i**2 for i in range(1, int(math.sqrt(n))+1)]  # 先找出n以内完全平方数
        
        def minSquareFunc(x):  # 递归
            if x in squareList:  # 如果在完全平方数list，则直接返回1
                return 1
            res = float('inf')  # 记住最小步数
            for squre in squareList:  # 遍历完全平方数list
                if x < squre:
                    break
                new_res = minSquareFunc(x-squre) + 1  # 对每个square都找出最小步数
                res = min(res, new_res)  # 比较目前最小步数和找出的最小步数
            return res
        
        return minSquareFunc(n)
# leetcode submit region end(Prohibit modification and deletion)
