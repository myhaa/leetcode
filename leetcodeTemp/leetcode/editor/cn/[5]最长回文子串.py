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
#  👍 3721 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 中心拓展法：
# 遍历每个中心，然后往两边拓展，直到不能拓展成回文串为止，记录当前回文串
# 分奇数和偶数情况，所以有两次循环
# 时间复杂度：O(N^2)
# 空间复杂度：O(1)
# 		执行耗时:1004 ms,击败了68.76% 的Python3用户
# 		内存消耗:15 MB,击败了65.83% 的Python3用户
class Solution:
    def is_huiwen(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return i+1, j-1
    
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        
        b0, e0 = 0, 0
        for i in range(n):
            b1, e1 = self.is_huiwen(s, i, i)
            b2, e2 = self.is_huiwen(s, i, i+1)
            if e1-b1 >= e0-b0:
                b0, e0 = b1, e1
            if e2-b2 >= e0-b0:
                b0, e0 = b2, e2
        return s[b0:e0+1]
# leetcode submit region end(Prohibit modification and deletion)
