# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
#
#  例如，
#
#      1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#     ...
#
#
#  示例 1:
#
#  输入: 1
# 输出: "A"
#
#
#  示例 2:
#
#  输入: 28
# 输出: "AB"
#
#
#  示例 3:
#
#  输入: 701
# 输出: "ZY"
#
#  Related Topics 数学
#  👍 314 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while n:
            n -= 1
            n, y = divmod(n, 26)
            res = chr(y + 65) + res
        return res
# leetcode submit region end(Prohibit modification and deletion)
