# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
#
#  给出两个整数 x 和 y，计算它们之间的汉明距离。
#
#  注意：
# 0 ≤ x, y < 231.
#
#  示例:
#
#
# 输入: x = 1, y = 4
#
# 输出: 2
#
# 解释:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#
# 上面的箭头指出了对应二进制位不同的位置。
#
#  Related Topics 位运算
#  👍 377 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 我算的
# class Solution:
#     def hammingDistance(self, x: int, y: int) -> int:
#         n = max(len(bin(x))-1, len(bin(y))-1)
#         res = 0
#         for i in range(n):
#             if bin(x)[-1] != bin(y)[-1]:
#                 res += 1
#             x >>= 1
#             y >>= 1
#         return res

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')



# leetcode submit region end(Prohibit modification and deletion)
