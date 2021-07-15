# 给你一个整数 n ，请你找出并返回第 n 个 丑数 。
#
#  丑数 就是只包含质因数 2、3 和/或 5 的正整数。
#
#
#
#  示例 1：
#
#
# 输入：n = 10
# 输出：12
# 解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
#
#
#  示例 2：
#
#
# 输入：n = 1
# 输出：1
# 解释：1 通常被视为丑数。
#
#
#
#
#  提示：
#
#
#  1 <= n <= 1690
#
#  Related Topics 哈希表 数学 动态规划 堆（优先队列）
#  👍 688 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1, 1]
        p2, p3, p5 = 1, 1, 1
        for i in range(2, n+1):
            num2 = 2*dp[p2]
            num3 = 3*dp[p3]
            num5 = 5*dp[p5]
            dp.append(min(num2, num3, num5))
            if dp[i] == num2:
                p2 += 1
            if dp[i] == num3:
                p3 += 1
            if dp[i] == num5:
                p5 += 1
        # print(dp)
        return dp[n]
# leetcode submit region end(Prohibit modification and deletion)
