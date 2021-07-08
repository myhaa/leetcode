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
#  Related Topics 贪心 数组 双指针
#  👍 2588 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 思路： 双重for循环，找到最大值
# 时间复杂度：O(N^2)
# 空间复杂度：O(1)
# 提交结果：Time Limit Exceeded
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         res = 0
#         n = len(height)
#         for i in range(n-1):
#             for j in range(i+1, n):
#                 res = max(res, min(height[i], height[j])*(j-i))
#         return res


# 思路：双指针
# 左指针指向头，右指针指向尾，计算容器容积，然后移动值较小那边的指针，继续计算
# 时间复杂度：O(N)
# 空间复杂度：O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        i, j = 0, n-1
        while i < j:
            res = max(res, min(height[i], height[j])*(j-i))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
