# 给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。
#
#  假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,3,4,2,2]
# 输出：2
#
#
#  示例 2：
#
#
# 输入：nums = [3,1,3,4,2]
# 输出：3
#
#
#  示例 3：
#
#
# 输入：nums = [1,1]
# 输出：1
#
#
#  示例 4：
#
#
# 输入：nums = [1,1,2]
# 输出：1
#
#
#
#
#  提示：
#
#
#  2 <= n <= 3 * 104
#  nums.length == n + 1
#  1 <= nums[i] <= n
#  nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次
#
#
#
#
#  进阶：
#
#
#  如何证明 nums 中至少存在一个重复的数字?
#  你可以在不修改数组 nums 的情况下解决这个问题吗？
#  你可以只用常量级 O(1) 的额外空间解决这个问题吗？
#  你可以设计一个时间复杂度小于 O(n2) 的解决方案吗？
#
#  Related Topics 数组 双指针 二分查找
#  👍 1227 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# # 超时
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         for i in range(len(nums)):
#             if nums[i] in nums[i+1:]:
#                 return nums[i]
#         return -1
#


# 运用字典存储
# 时间复杂度：O(N)
# 空间复杂度：O(N)
# 			执行耗时:124 ms,击败了21.33% 的Python3用户
# 			内存消耗:30.3 MB,击败了5.01% 的Python3用户
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         tmp = {}
#         for i in nums:
#             if tmp.get(i, None) is None:
#                 tmp[i] = 0
#             else:
#                 return i
#         return -1
#
# 双指针
# 将数组构建为图，使用环形链表判断是否有环的方法
# 时间复杂度：O(N)
# 空间复杂度：O(1)
# 			执行耗时:104 ms,击败了25.33% 的Python3用户
# 			内存消耗:25.5 MB,击败了21.78% 的Python3用户
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         slow, fast = 0, 0
#         slow = nums[slow]
#         fast = nums[nums[fast]]
#         while slow != fast:
#             slow = nums[slow]
#             fast = nums[nums[fast]]
#         slow = 0
#         while slow != fast:
#             slow = nums[slow]
#             fast = nums[fast]
#         return slow

# 二分查找

# 			执行耗时:376 ms,击败了9.85% 的Python3用户
# 			内存消耗:25.6 MB,击败了12.71% 的Python3用户
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l, r = 1, len(nums)-1
        ans = -1
        while l <= r:
            mid = (l+r) >> 1
            cur = 0
            for i in nums:
                if i <= mid:
                    cur += 1
            if cur <= mid:
                l = mid + 1
            else:
                r = mid - 1
                ans = mid
        return ans
# leetcode submit region end(Prohibit modification and deletion)
