# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
#  示例 1:
#
#  输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
#
#
#  示例 2:
#
#  输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
#
#  说明:
#
#  你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
#  Related Topics 堆 分治算法
#  👍 1072 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 直接利用python函数sort
# 			执行耗时:40 ms,击败了91.88% 的Python3用户
# 			内存消耗:15.2 MB,击败了90.46% 的Python3用户
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         return nums[-1*k]

# 大根堆解法
# 			执行耗时:92 ms,击败了43.90% 的Python3用户
# 			内存消耗:15.3 MB,击败了66.59% 的Python3用户
class Solution:
    def heapify(self, nums, n, i):
        largest = i
        l, r = 2 * i + 1, 2 * i + 2
        
        if l < n and  nums[l] > nums[largest]:
            largest = l
        if r < n and nums[r] > nums[largest]:
            largest = r
        
        if largest != i:
            nums[largest], nums[i] = nums[i], nums[largest]
            self.heapify(nums, n, largest)
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        for i in range(n-1, -1, -1):
            self.heapify(nums, n, i)
        
        for i in range(n-1, n-k, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums, i, 0)
        return nums[0]
    

# leetcode submit region end(Prohibit modification and deletion)
