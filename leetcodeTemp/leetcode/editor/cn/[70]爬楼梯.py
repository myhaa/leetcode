# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。 
# 
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？ 
# 
#  注意：给定 n 是一个正整数。 
# 
#  示例 1： 
# 
#  输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶 
# 
#  示例 2： 
# 
#  输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#  
#  Related Topics 动态规划 
#  👍 1434 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 时间超出限制
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n
#         return self.climbStairs(n-1) + self.climbStairs(n-2)
#

# # 还是有点慢
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         p,q,r = 0,0,1
#         for i in range(1, n+1):
#             p = q
#             q = r
#             r = p+q
#         return r
# 通项公式：f(n)=f(n-1)+f(n-2)
import math
class Solution:
    def climbStairs(self, n: int) -> int:
        r = int(round((1/math.sqrt(5))*(((1+math.sqrt(5))/2)**(n+1) - ((1-math.sqrt(5)/2))**(n+1))))
        return r
# leetcode submit region end(Prohibit modification and deletion)


test = Solution()
print(test.climbStairs(2))
print(test.climbStairs(3))
print(test.climbStairs(4))
print(test.climbStairs(5))
print(test.climbStairs(10))
print(test.climbStairs(44))
