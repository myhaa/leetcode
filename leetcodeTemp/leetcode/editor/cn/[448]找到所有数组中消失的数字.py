# 给定一个范围在 1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
#
#  找到所有在 [1, n] 范围之间没有出现在数组中的数字。
#
#  您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。
#
#  示例:
#
#
# 输入:
# [4,3,2,7,8,2,3,1]
#
# 输出:
# [5,6]
#
#  Related Topics 数组
#  👍 651 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in nums:
            x = (i-1) % n  # 每个位置上的数字减一再取模
            nums[x] += n  # 再在该位置加上n，不影响取模，但是后面可以判断该位置是否大于n，来判断数字是否在数组里
        res = [i+1 for i, j in enumerate(nums) if j <= n]
        return res

# leetcode submit region end(Prohibit modification and deletion)
