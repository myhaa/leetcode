# date: 2021-03-04 22:37:06

# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
#
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#
#  你可以按任意顺序返回答案。
#
#
#
#  示例 1：
#
#
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
#
#
#  示例 2：
#
#
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
#
#
#  示例 3：
#
#
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#
#
#
#
#  提示：
#
#
#  2 <= nums.length <= 103
#  -109 <= nums[i] <= 109
#  -109 <= target <= 109
#  只会存在一个有效答案
#
#  Related Topics 数组 哈希表
#  👍 10433 👎 0

# test
# leetcode submit region begin(Prohibit modification and deletion)
# 第一种：暴力求解，双重循环
# 时间复杂度：O(N^2)
# 空间复杂度：O(1)

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         for i in range(n-1):
#             for j in range(i+1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []

# 第二种：hash表
# 时间复杂度：O(N)
# 空间复杂度：O(N)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hash_table = dict()

        for i, num in enumerate(nums):
            if target - num in hash_table:
                return [i, hash_table[target-num]]
            hash_table[num] = i
        return []
# leetcode submit region end(Prohibit modification and deletion)
