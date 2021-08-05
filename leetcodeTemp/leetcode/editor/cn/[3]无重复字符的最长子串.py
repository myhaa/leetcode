# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
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
#  Related Topics 哈希表 字符串 滑动窗口
#  👍 5862 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 暴力枚举
# 时间复杂度：O(N^2)
# 空间复杂度：O(1)
# 		执行耗时:340 ms,击败了13.07% 的Python3用户
# 		内存消耗:15 MB,击败了50.54% 的Python3用户
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         n = len(s)
#         if n <= 1:
#             return n
#         res = 0
#         for i in range(n-1):
#             count = 0
#             for j in range(i, n):
#                 if s[j] not in s[i:j]:
#                     count += 1
#                 else:
#                     break
#             res = max(res, count)
#         return res

# 优化 滑动窗口+hashset
# i从0到n-1遍历，rk是最长连续无重复字串的右端点，i+1，则hashset移除该元素，rk+1，则添加元素，且无重复
# 这样就避免计算那些明显小于长度的无效计算
# 时间复杂度：O(N)
# 空间复杂度：O(字符集数量)
#       执行耗时:88 ms,击败了33.92% 的Python3用户
# 		内存消耗:15.1 MB,击败了20.88% 的Python3用户
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        rk, res = -1, 0  # rk从-1开始代表还没有移动
        hashset = set()
        for i in range(n):
            if i != 0:
                hashset.remove(s[i-1])
            while rk + 1 < n and s[rk+1] not in hashset:  # 不断右移rk指针
                hashset.add(s[rk+1])
                rk += 1
            res = max(res, rk + 1 - i)
        return res

# leetcode submit region end(Prohibit modification and deletion)
