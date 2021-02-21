# 给定一个已按照 升序排列 的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。
#
#  函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0]
#  < answer[1] <= numbers.length 。
#
#  你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
#
#
#  示例 1：
#
#
# 输入：numbers = [2,7,11,15], target = 9
# 输出：[1,2]
# 解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
#
#
#  示例 2：
#
#
# 输入：numbers = [2,3,4], target = 6
# 输出：[1,3]
#
#
#  示例 3：
#
#
# 输入：numbers = [-1,0], target = -1
# 输出：[1,2]
#
#
#
#
#  提示：
#
#
#  2 <= numbers.length <= 3 * 104
#  -1000 <= numbers[i] <= 1000
#  numbers 按 递增顺序 排列
#  -1000 <= target <= 1000
#  仅存在一个有效答案
#
#  Related Topics 数组 双指针 二分查找
#  👍 478 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         left, right = 0, len(numbers)-1
#         while left < right:
#             tmp = numbers[left] + numbers[right]
#             if tmp == target:
#                 return [left+1, right+1]
#             elif tmp < target:
#                 left += 1
#             else:
#                 right -= 1
#         return [-1, -1]


class Solution:
	def twoSum(self, numbers: List[int], target: int) -> List[int]:
		def search(arr, left, right, x):
			if left > right:
				return -1
			mid = (left + right) // 2
			if arr[mid] == x:
				return mid
			elif arr[mid] < x:
				return search(arr, mid+1, right, x)
			else:
				return search(arr, left, mid-1, x)
		for i in range(len(numbers)):
			j = search(numbers, i+1, len(numbers)-1, target-numbers[i])
			if j != -1:
				return [i+1, j+1]
		return [-1, -  1]
# leetcode submit region end(Prohibit modification and deletion)
