# date: 2021-03-09 23:30:43

# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
#
#
#  示例 1:
#
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#
#  示例 2:
#
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#
#  示例 3:
#
#
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#
#  示例 4:
#
#
# 输入: s = ""
# 输出: 0
#
#
#
#
#  提示：
#
#
#  0 <= s.length <= 5 * 104
#  s 由英文字母、数字、符号和空格组成
#
#  Related Topics 哈希表 双指针 字符串 Sliding Window
#  👍 5098 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 自己的解法
# 时间复杂度：O(N^2)
# 耗时
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s = len(s)
        if len_s <= 1:
            return len_s
        p,  q, res = 0, 1, 1
        while q < len_s:
            tmp = s[p:q+1]
            if len(set(tmp)) == len(tmp):
                q += 1
                res = max(res, q-p)
            else:
                p += 1
                q = p + 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
