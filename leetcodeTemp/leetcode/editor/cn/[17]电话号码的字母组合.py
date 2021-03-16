# date: 2021-03-15 23:29:21

# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
#
#  给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
#
#
#
#  示例 1：
#
#
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
#
#  示例 2：
#
#
# 输入：digits = ""
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：digits = "2"
# 输出：["a","b","c"]
#
#
#
#
#  提示：
#
#
#  0 <= digits.length <= 4
#  digits[i] 是范围 ['2', '9'] 的一个数字。
#
#  Related Topics 深度优先搜索 递归 字符串 回溯算法
#  👍 1178 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 递归
# 时间复杂度：O(N^2)
# 空间复杂度：O(N)
# 执行耗时:32 ms,击败了94.27% 的Python3用户
# 内存消耗:15 MB,击败了21.63% 的Python3用户
class Solution:
    def __init__(self):
        self.digitsDict = {
            '2': list('abc'),
            '3': list('def'),
            '4': list('ghi'),
            '5': list('jkl'),
            '6': list('mno'),
            '7': list('pqrs'),
            '8': list('tuv'),
            '9': list('wxyz')
        }
        
    def letterCombinations(self, digits: str) -> List[str]:
        len_digits = len(digits)
        if len_digits <= 1:
            return self.digitsDict.get(digits, [])
        tmp = self.digitsDict.get(digits[0], [])
        rest = self.letterCombinations(digits[1:])
        return [x+y for x in tmp for y in rest]
        
# leetcode submit region end(Prohibit modification and deletion)
