# date: 2021-03-25 22:58:07

# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
#  示例:
#
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#  Related Topics 回溯算法
#  👍 1242 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 回溯算法
# 执行耗时:28 ms,击败了99.74% 的Python3用户
# 内存消耗:15 MB,击败了59.91% 的Python3用户
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack():
            # print(combination)
            if len(combination) == len(nums):
                combinations.append(combination[:])
                return
            else:
                for i in nums:
                    if i not in combination:
                        combination.append(i)
                        backtrack()
                        combination.pop()
        combination = list()
        combinations = list()
        backtrack()
        return combinations
# leetcode submit region end(Prohibit modification and deletion)
