# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
#  说明：
#
#  你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
#  示例 1:
#
#  输入: [2,2,1]
# 输出: 1
#
#
#  示例 2:
#
#  输入: [4,1,2,1,2]
# 输出: 4
#  Related Topics 位运算 哈希表
#  👍 1694 👎 0

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         res = []
#         for i in nums:
#             if i in res:
#                 res.remove(i)
#             else:
#                 res.append(i)
#         return res[0]

# 异或运算i
from functools import reduce
class Solution:
	def singleNumber(self, nums: List[int]) -> int:
		# res = nums[0]
		# for i in nums[1:]:
		# 	res ^= i
		return reduce(lambda x,y:x^y, nums)
# leetcode submit region end(Prohibit modification and deletion)
