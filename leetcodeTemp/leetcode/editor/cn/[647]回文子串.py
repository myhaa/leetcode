# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
#
#  具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
#
#
#
#  示例 1：
#
#  输入："abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
#
#
#  示例 2：
#
#  输入："aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
#
#
#
#  提示：
#
#
#  输入的字符串长度不会超过 1000 。
#
#  Related Topics 字符串 动态规划
#  👍 603 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 最简单得解法：列出所有字串，然后判断是否是回文串
# 时间复杂度：O(N^3)
# 空间复杂度：O(N^2)
# 			执行耗时:628 ms,击败了6.60% 的Python3用户
# 			内存消耗:213.2 MB,击败了5.04% 的Python3用户
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         n = len(s)
#         if n <= 1:
#             return n
#         res = []
#         for i in range(n):
#             for j in range(i+1, n+1):
#                 res.append(s[i:j])
#
#         ans = 0
#         for i in res:
#             if i == i[::-1]:
#                 ans += 1
#         return ans

# 中心拓展法
# 遍历每个中心点，然后往两边拓展
# 时间复杂度：O(N^2)
# 空间复杂度：O(1)
class Solution:
    def is_huiwen(self, s, i, j, tmp):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            tmp += 1
            i -= 1
            j += 1
        return tmp
    
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        ans = 0
        for i in range(n):
            ans = self.is_huiwen(s, i, i, tmp=ans)
            ans = self.is_huiwen(s, i, i+1, tmp=ans)
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
