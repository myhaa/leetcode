# date: 2021-03-16 23:50:53

# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
#
#  有效字符串需满足：
#
#
#  左括号必须用相同类型的右括号闭合。
#  左括号必须以正确的顺序闭合。
#
#
#
#
#  示例 1：
#
#
# 输入：s = "()"
# 输出：true
#
#
#  示例 2：
#
#
# 输入：s = "()[]{}"
# 输出：true
#
#
#  示例 3：
#
#
# 输入：s = "(]"
# 输出：false
#
#
#  示例 4：
#
#
# 输入：s = "([)]"
# 输出：false
#
#
#  示例 5：
#
#
# 输入：s = "{[]}"
# 输出：true
#
#
#
#  提示：
#
#
#  1 <= s.length <= 104
#  s 仅由括号 '()[]{}' 组成
#
#  Related Topics 栈 字符串
#  👍 2240 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 时间复杂度：O(N)
# 空间复杂度：O(N)
# 执行耗时:36 ms,击败了85.80% 的Python3用户
# 内存消耗:14.9 MB,击败了46.36% 的Python3用户
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        tmp_dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        res = []
        for i in s:
            if i in tmp_dict:
                if not res or tmp_dict[i] != res[-1]:
                    return False
                res.pop()
            else:
                res.append(i)
        return not res
        
# leetcode submit region end(Prohibit modification and deletion)
