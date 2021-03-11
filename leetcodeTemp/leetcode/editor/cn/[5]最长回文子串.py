# date: 2021-03-10 23:23:41

# 给你一个字符串 s，找到 s 中最长的回文子串。
#
#
#
#  示例 1：
#
#
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#
#
#  示例 2：
#
#
# 输入：s = "cbbd"
# 输出："bb"
#
#
#  示例 3：
#
#
# 输入：s = "a"
# 输出："a"
#
#
#  示例 4：
#
#
# 输入：s = "ac"
# 输出："a"
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 1000
#  s 仅由数字和英文字母（大写和/或小写）组成
#
#  Related Topics 字符串 动态规划
#  👍 3322 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 我的解法，依次遍历，枚举每个子串，判断其是否回文串
# 时间复杂度：O(N^2)
# 执行耗时:9672 ms,击败了4.99% 的Python3用户
# 内存消耗:14.7 MB,击败了89.83% 的Python3用户
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         if s == s[::-1]:
#             return s
#         len_s = len(s)
#         res = s[0]
#         for i in range(len_s):
#             j = i + 1
#             while j < len_s:
#                 tmp = s[i:j+1]
#                 if tmp == tmp[::-1] and len(tmp) > len(res):
#                     res = tmp
#                 else:
#                     j += 1
#         return res

# 优化-中心拓展法
# 时间复杂度：O(N^2)
# 执行耗时:1000 ms,击败了63.72% 的Python3用户
# 内存消耗:14.7 MB,击败了91.21% 的Python3用户
class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left+1, right-1
        
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i+1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end+1]
    
# leetcode submit region end(Prohibit modification and deletion)
