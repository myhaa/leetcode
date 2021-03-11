# date: 2021-03-11 22:27:09

# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
# ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
#  说明：你不能倾斜容器。
#
#
#
#  示例 1：
#
#
#
#
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
# 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
#
#  示例 2：
#
#
# 输入：height = [1,1]
# 输出：1
#
#
#  示例 3：
#
#
# 输入：height = [4,3,2,1,4]
# 输出：16
#
#
#  示例 4：
#
#
# 输入：height = [1,2,1]
# 输出：2
#
#
#
#
#  提示：
#
#
#  n = height.length
#  2 <= n <= 3 * 104
#  0 <= height[i] <= 3 * 104
#
#  Related Topics 数组 双指针
#  👍 2257 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 超时：
# 时间复杂度：O(N^2)
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         p, q, res = 0, 1, 0
#         while p < len(height)-1:
#             while q < len(height):
#                 tmp = min(height[p], height[q])
#                 res = max(res, tmp*(q-p))
#                 q += 1
#             p += 1
#             q = p + 1
#         return res

# 双指针，解答成功
# 时间复杂度: O(N)
# 执行耗时:280 ms,击败了5.54% 的Python3用户
# 内存消耗:24.6 MB,击败了5.11% 的Python3用户
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, res = 0, len(height)-1, 0
        while left < right:
            tmp = min(height[left], height[right])
            res = max(res, tmp*(right-left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
