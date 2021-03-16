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
# class Solution:
#     def __init__(self):
#         self.digitsDict = {
#             '2': list('abc'),
#             '3': list('def'),
#             '4': list('ghi'),
#             '5': list('jkl'),
#             '6': list('mno'),
#             '7': list('pqrs'),
#             '8': list('tuv'),
#             '9': list('wxyz')
#         }
#
#     def letterCombinations(self, digits: str) -> List[str]:
#         len_digits = len(digits)
#         if len_digits <= 1:
#             return self.digitsDict.get(digits, [])
#         tmp = self.digitsDict.get(digits[0], [])
#         rest = self.letterCombinations(digits[1:])
#         return [x+y for x in tmp for y in rest]

# 迭代版
# 执行耗时:44 ms,击败了30.15% 的Python3用户
# 内存消耗:14.8 MB,击败了77.07% 的Python3用户
# class Solution:
#     def __init__(self):
#         self.digitsDict = {
#             '2': list('abc'),
#             '3': list('def'),
#             '4': list('ghi'),
#             '5': list('jkl'),
#             '6': list('mno'),
#             '7': list('pqrs'),
#             '8': list('tuv'),
#             '9': list('wxyz')
#         }
#
#     def letterCombinations(self, digits: str) -> List[str]:
#         len_digits = len(digits)
#         if len_digits <= 1:
#             return self.digitsDict.get(digits, [])
#         q = len_digits - 2
#         right = self.digitsDict.get(digits[-1], [])
#         while q >= 0:
#             tmp = self.digitsDict.get(digits[q], [])
#             right = [x+y for x in tmp for y in right]
#             q -= 1
#         return right

# 官方解答
# 时间复杂度：O(3^m+4^n)
# 空间复杂度：O(m+n)
# 执行耗时:44 ms,击败了30.15% 的Python3用户
# 内存消耗:14.9 MB,击败了47.65% 的Python3用户
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return list()
        
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        def backtrack(index: int):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()
        
        combination = list()
        combinations = list()
        backtrack(0)
        return combinations

# leetcode submit region end(Prohibit modification and deletion)
