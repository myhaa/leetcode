# date: 2021-03-27 22:37:26

# 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
#
#  数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
#  判断你是否能够到达最后一个下标。
#
#
#
#  示例 1：
#
#
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
#
#
#  示例 2：
#
#
# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 3 * 104
#  0 <= nums[i] <= 105
#
#  Related Topics 贪心算法 数组
#  👍 1107 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# # 超时! 超时！ 超时！
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#
#         res = [1]
#         for i in range(1, len(nums)):
#             res.append(0)
#             for j in range(i):
#                 if res[j] and j + nums[j] >= i:
#                     res[i] = 1
#                     break
#         return True if res[-1] > 0 else False

# 贪心
# 时间O(N) 空间O(1)
# 执行耗时:68 ms,击败了8.11% 的Python3用户
# 内存消耗:16 MB,击败了44.86% 的Python3用户
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right_max = 0
        for i, num in enumerate(nums):
            if i <= right_max:
                right_max = max(right_max, i + num)
                if right_max >= len(nums)-1:
                    return True
        return False
        
# leetcode submit region end(Prohibit modification and deletion)
