# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
#
#  解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
#  示例 2：
#
#
# 输入：nums = [0]
# 输出：[[],[0]]
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10
#  -10 <= nums[i] <= 10
#  nums 中的所有元素 互不相同
#
#  Related Topics 位运算 数组 回溯算法
#  👍 1207 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 递归思路
# for i in range(n): 在每个i上都可以选择要不要当前位置上的数

# 时间复杂度： O(2^N)
# 空间复杂度： O(N)
# 		执行耗时:36 ms,击败了85.76% 的Python3用户
# 		内存消耗:14.7 MB,击败了95.77% 的Python3用户
# class Solution:
#     def f(self, nums, i, res):
#         if i == len(nums):
#             ans.append(res)
#             return
#         self.f(nums, i+1, res)
#         self.f(nums, i+1, res+[nums[i]])
#
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         global ans
#         ans = []
#         self.f(nums, 0, [])
#         return ans

# 回溯算法
#		执行耗时:44 ms,击败了38.81% 的Python3用户
#		内存消耗:15.1 MB,击败了23.49% 的Python3用户
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         def traceback(index):
#             ans.append(res[:])
#             for i in range(index, len(nums)):
#                 res.append(nums[i])
#                 traceback(i+1)
#                 res.pop()
#         ans = []
#         res = []
#         traceback(0)
#         return ans

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         def traceback(index, tmp):
#             ans.append(tmp)
#             for i in range(index, len(nums)):
#                 traceback(i+1, tmp+[nums[i]])
#         ans = []
#         traceback(0, [])
#         return ans

# 数组迭代
#		执行耗时:36 ms,击败了85.76% 的Python3用户
#		内存消耗:15 MB,击败了52.36% 的Python3用户
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            res += [x+[i] for x in res]
        return res
# leetcode submit region end(Prohibit modification and deletion)
