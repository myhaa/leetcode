# date: 2021-03-17 23:08:09

# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
#  示例 1：
#
#
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
#
#
#  示例 2：
#
#
# 输入：n = 1
# 输出：["()"]
#
#
#
#
#  提示：
#
#
#  1 <= n <= 8
#
#  Related Topics 字符串 回溯算法
#  👍 1639 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 回溯法，记住左括号和右括号的数量
# 		执行耗时:32 ms,击败了97.15% 的Python3用户
# 		内存消耗:15 MB,击败了81.05% 的Python3用户
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(s, left, right):
            if len(s) == n*2:
                res.append(''.join(s))
                return
            if left < n:
                s.append('(')
                backtrack(s, left+1, right)
                s.pop()
            if right < left:
                s.append(')')
                backtrack(s, left, right+1)
                s.pop()
            
        backtrack([], 0, 0)
        return res
        
        
# leetcode submit region end(Prohibit modification and deletion)
