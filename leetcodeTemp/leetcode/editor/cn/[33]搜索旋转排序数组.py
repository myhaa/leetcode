# date: 2021-03-22 22:52:02

# 整数数组 nums 按升序排列，数组中的值 互不相同 。
#
#  在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[
# k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2
# ,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
#
#  给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的索引，否则返回 -1 。
#
#
#
#  示例 1：
#
#
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
#
#
#  示例 2：
#
#
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
#
#  示例 3：
#
#
# 输入：nums = [1], target = 0
# 输出：-1
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 5000
#  -10^4 <= nums[i] <= 10^4
#  nums 中的每个值都 独一无二
#  nums 肯定会在某个点上旋转
#  -10^4 <= target <= 10^4
#
#
#
#
#  进阶：你可以设计一个时间复杂度为 O(log n) 的解决方案吗？
#  Related Topics 数组 二分查找
#  👍 1242 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 方法一：二分查找
#
# **思路和算法**
#
# 对于有序数组，可以使用二分查找的方法查找元素。
#
# 但是这道题中，数组本身不是有序的，进行旋转后只保证了数组的局部是有序的，这还能进行二分查找吗？答案是可以的。
#
# 可以发现的是，我们将数组从中间分开成左右两部分的时候，一定有一部分的数组是有序的。
# 拿示例来看，我们从 `6` 这个位置分开以后数组变成了 `[4, 5, 6]` 和 `[7, 0, 1, 2]` 两个部分，其中左边 `[4, 5, 6]` 这个部分的数组是有序的，其他也是如此。
#
# 这启示我们可以在常规二分查找的时候查看当前 `mid` 为分割位置分割出来的两个部分 `[l, mid]` 和 `[mid + 1, r]` 哪个部分是有序的，
# 并根据有序的那个部分确定我们该如何改变二分查找的上下界，因为我们能够根据有序的那部分判断出 `target` 在不在这个部分：
#
# - 如果 `[l, mid - 1]` 是有序数组，且 `target` 的大小满足
# ![\[\textit{nums}\[l\],\textit{nums}\[mid\]) ](./p___textit{nums}_l_,textit{nums}_mid___.png) ，
# 则我们应该将搜索范围缩小至 `[l, mid - 1]`，否则在 `[mid + 1, r]` 中寻找。
# - 如果 `[mid, r]` 是有序数组，且 `target` 的大小满足
# ![(\textit{nums}\[mid+1\],\textit{nums}\[r\]\] ](./p___textit{nums}_mid+1_,textit{nums}_r___.png) ，
# 则我们应该将搜索范围缩小至 `[mid + 1, r]`，否则在 `[l, mid - 1]` 中寻找。
#
# ![fig1](https://assets.leetcode-cn.com/solution-static/33/33_fig1.png)
#
# 需要注意的是，二分的写法有很多种，所以在判断 `target` 大小与有序部分的关系的时候可能会出现细节上的差别。
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) >> 1
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
# leetcode submit region end(Prohibit modification and deletion)
