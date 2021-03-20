# date: 2021-03-19 22:59:33

# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
#
#
#  示例 1：
#
#
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
#
#
#  示例 2：
#
#
# 输入：nums = [1]
# 输出：1
#
#
#  示例 3：
#
#
# 输入：nums = [0]
# 输出：0
#
#
#  示例 4：
#
#
# 输入：nums = [-1]
# 输出：-1
#
#
#  示例 5：
#
#
# 输入：nums = [-100000]
# 输出：-100000
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 3 * 104
#  -105 <= nums[i] <= 105
#
#
#
#
#  进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。
#  Related Topics 数组 分治算法 动态规划
#  👍 3021 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums == 1:
            return nums[0]
        mid = len_nums >> 1
        left = self.maxSubArray(nums[:mid])
        right = self.maxSubArray(nums[mid:])
        left_max = nums[mid-1]
        tmp = left_max
        for i in range(mid-1-1, -1, -1):
            tmp += nums[i]
            left_max = max(left_max, tmp)
        right_max = nums[mid]
        tmp = right_max
        for i in nums[mid+1:]:
            tmp += i
            right_max = max(right_max, tmp)
        return max(left, right, left_max+right_max)
# leetcode submit region end(Prohibit modification and deletion)
