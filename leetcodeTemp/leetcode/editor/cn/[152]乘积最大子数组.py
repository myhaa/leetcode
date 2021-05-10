# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
#
#
#
#  示例 1:
#
#  输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#
#
#  示例 2:
#
#  输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
#  Related Topics 数组 动态规划
#  👍 1088 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 时间复杂度：O(N)
# 空间复杂度：O(1)
# 			执行耗时:48 ms,击败了75.27% 的Python3用户
# 			内存消耗:14.9 MB,击败了90.54% 的Python3用户
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_, min_, ans = nums[0], nums[0], nums[0]
        for i in nums[1:]:
            mx, mn = max_, min_
            max_ = max([mx*i, i, mn*i])
            min_ = min([mn*i, i, mx*i])
            ans = max(max_, ans)
        return ans
        
        
# leetcode submit region end(Prohibit modification and deletion)
