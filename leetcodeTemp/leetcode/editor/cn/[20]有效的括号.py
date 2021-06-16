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
#  👍 2453 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 栈
# 思路：
# 将符号做成一个dict，然后遍历字符串，判断该字符是否在dict中，如果在则与栈中元素对比，如果不在，则加入栈
# 实践复杂度：O(n)
# 空间复杂度：O(n)
# 		执行耗时:36 ms,击败了86.99% 的Python3用户
# 		内存消耗:15.1 MB,击败了5.60% 的Python3用户
class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n <= 1:
            return False
        s_dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for i in s:
            if i not in s_dict.keys():
                stack.append(i)
            else:
                if stack and s_dict.get(i) == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:  # 判断栈是否为空
            return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
