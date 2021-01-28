# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。 
# 
#  初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nu
# ms2 的元素。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums1 = [1], m = 1, nums2 = [], n = 0
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  nums1.length == m + n 
#  nums2.length == n 
#  0 <= m, n <= 200 
#  1 <= m + n <= 200 
#  -109 <= nums1[i], nums2[i] <= 109 
#  
#  Related Topics 数组 双指针 
#  👍 747 👎 0

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
# 自己的解答
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         解答思路：双指针，left和right值比较，如果left<=right，left++
#         反之则将m+j~i依次往后移动，然后left++，right++
#         重点就是边界问题
#         """
#         if n > 0:
#             i, j = 0, 0
#             while i < (m+n) and j < n:
#                 if nums1[i] <= nums2[j]:
#                     i += 1
#                 else:
#                     x = m+j
#                     while x > i:
#                         nums1[x] = nums1[x-1]
#                         x -=1
#                     nums1[i] = nums2[j]
#                     j+=1
#                     i+=1
#             nums1[(m+j):] = nums2[j:]

# 别人的解答，时间：O(n+m), 空间:O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        解答思路：双指针，left和right值比较，如果left<=right，left++
        反之则将m+j~i依次往后移动，然后left++，right++
        重点就是边界问题
        """
        p1, p2, p = m-1, n-1, m+n-1
        while p1>=0 and p2 >=0:
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        nums1[:p2+1] = nums2[:p2+1]
# leetcode submit region end(Prohibit modification and deletion)
