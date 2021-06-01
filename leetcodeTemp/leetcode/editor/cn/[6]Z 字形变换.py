# date: 2021-05-31 23:29:34

# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
#
#  比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
#
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
#  之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
#
#  请你实现这个将字符串进行指定行数变换的函数：
#
#
# string convert(string s, int numRows);
#
#
#
#  示例 1：
#
#
# 输入：s = "PAYPALISHIRING", numRows = 3
# 输出："PAHNAPLSIIGYIR"
#
# 示例 2：
#
#
# 输入：s = "PAYPALISHIRING", numRows = 4
# 输出："PINALSIGYAHRPI"
# 解释：
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#
#
#  示例 3：
#
#
# 输入：s = "A", numRows = 1
# 输出："A"
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 1000
#  s 由英文字母（小写和大写）、',' 和 '.' 组成
#  1 <= numRows <= 1000
#
#  Related Topics 字符串
#  👍 1162 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 时间复杂度：O(N)
# 空间复杂度：O(N)
# 		执行耗时:68 ms,击败了54.91% 的Python3用户
# 		内存消耗:14.9 MB,击败了84.82% 的Python3用户
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if len(s) == 1 or numRows == 1:
#             return s
#         res = {}
#         for i in range(numRows):
#             res[i] = []
#         i, j = -1, -1
#         while i < len(s):
#             while j < numRows-1:
#                 j += 1
#                 i += 1
#                 if i >= len(s):
#                     break
#                 res[j].append(s[i])
#
#             while j > 0:
#                 j -= 1
#                 i += 1
#                 if i >= len(s):
#                     break
#                 res[j].append(s[i])
#         res1 = ''
#         for key, value in res.items():
#             value = ''.join(value)
#             res1 += value
#         return res1

# 			执行耗时:84 ms,击败了24.24% 的Python3用户
# 			内存消耗:15.1 MB,击败了37.39% 的Python3用户
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1:
            return s
        res = {}
        for i in range(numRows):
            res[i] = []
        count, flag = 0, -1
        for i in s:
            res[count].append(i)
            if count == 0 or count == (numRows-1):
                flag = -1 * flag
            count += flag
        res1 = ''
        for key, value in res.items():
            value = ''.join(value)
            res1 += value
        return res1
# leetcode submit region end(Prohibit modification and deletion)
