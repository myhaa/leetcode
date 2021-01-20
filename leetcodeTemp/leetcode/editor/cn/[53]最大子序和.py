# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。 
# 
#  示例: 
# 
#  输入: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#  
# 
#  进阶: 
# 
#  如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。 
#  Related Topics 数组 分治算法 动态规划 
#  👍 2810 👎 0

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
# 暴力解法
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         len_nums = len(nums)
#         if len_nums == 1:
#             return nums[0]
#
#         tmp = nums[0]
#         max_ = tmp
#         for i in range(1, len_nums):
#             if tmp + nums[i] > nums[i]:
#                 max_ = max(max_, tmp+nums[i])
#                 tmp = tmp + nums[i]
#             else:
#                 tmp = nums[i]
#                 max_ = max(max_, tmp)
#         return max_

# 分治
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums == 1:
            return nums[0]

        mid = len_nums // 2
        max_left = self.maxSubArray(nums[:mid])
        max_right = self.maxSubArray(nums[mid:])

        max_l = nums[mid - 1]
        tmp = max_l
        for i in range(mid-1-1, -1, -1):
            tmp += nums[i]
            max_l = max(max_l,tmp)
        max_r = nums[mid]
        tmp = max_r
        for i in nums[mid+1:]:
            tmp += i
            max_r = max(max_r, tmp)

        return max(max_left, max_right, max_l+max_r)



# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    test = Solution()
    print(test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
