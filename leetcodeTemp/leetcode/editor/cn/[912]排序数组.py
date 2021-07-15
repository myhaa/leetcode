# 给你一个整数数组 nums，请你将该数组升序排列。
#
#
#
#
#
#
#  示例 1：
#
#  输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
#
#
#  示例 2：
#
#  输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 50000
#  -50000 <= nums[i] <= 50000
#
#  Related Topics 数组 分治 桶排序 计数排序 基数排序 排序 堆（优先队列） 归并排序
#  👍 316 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import random


class Solution:
    
    def partition(self, nums, low, high):
        pivot = random.randint(low, high)
        nums[pivot], nums[high] = nums[high], nums[pivot]
        
        i = low - 1
        for j in range(low, high):
            if nums[j] <= nums[high]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        i += 1
        nums[i], nums[high] = nums[high], nums[i]
        return i
    
    def quicksort(self, nums, low, high):
        if low >= high:
            return
        mid = self.partition(nums, low, high)
        self.quicksort(nums, low, mid-1)
        self.quicksort(nums, mid+1, high)
    
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums)-1)
        return nums
# leetcode submit region end(Prohibit modification and deletion)
