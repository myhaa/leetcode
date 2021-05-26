# date: 2021-03-26 21:06:19

# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
#  子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序
# 列。
#
#
#  示例 1：
#
#
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
#
#
#  示例 2：
#
#
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
#
#
#  示例 3：
#
#
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 2500
#  -104 <= nums[i] <= 104
#
#
#
#
#  进阶：
#
#
#  你可以设计时间复杂度为 O(n2) 的解决方案吗？
#  你能将算法的时间复杂度降低到 O(n log(n)) 吗?
#
#  Related Topics 二分查找 动态规划
#  👍 1477 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 动态规划
# 转移：dp[i]= max(dp[i], dp[j]+1) for j in range(i) for i in range(1, len(nums)) if nums[i] > nums[j]
# 时间复杂度：O(N^2)
# 空间复杂度：O(N)
# 			执行耗时:3816 ms,击败了28.82% 的Python3用户
# 			内存消耗:15.1 MB,击败了60.36% 的Python3用户
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         dp = [1] * len(nums)
#         for i in range(1, len(nums)):
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], dp[j]+1)
#         return max(dp)


# 贪心+二分查找
# 维护一个数组dp, 保证数组dp递增，且dp长度，则是所求，
# 关键在于dp如何更新，则我们需要让序列上升得尽可能慢，因此我们希望每次在上升子序列最后加上的那个数尽可能的小
# 时间复杂度：O(nlogn)
# 空间复杂度：O(n)
# 			执行耗时:72 ms,击败了77.64% 的Python3用户
# 			内存消耗:15.2 MB,击败了8.27% 的Python3用户
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = []
        for i in nums:
            if not dp or dp[-1] < i:
                dp.append(i)
            else:
                l, r = 0, len(dp) - 1
                loc = r
                while l <= r:
                    mid = (l+r) >> 1
                    if dp[mid] >= i:
                        r = mid - 1
                        loc = mid
                    else:
                        l = mid + 1
                dp[loc] = i
        return len(dp)
        
# leetcode submit region end(Prohibit modification and deletion)
