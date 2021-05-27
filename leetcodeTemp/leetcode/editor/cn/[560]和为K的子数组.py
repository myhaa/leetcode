# date: 2021-05-27 22:11:39

# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
#
#  示例 1 :
#
#
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
#
#
#  说明 :
#
#
#  数组的长度为 [1, 20,000]。
#  数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
#
#  Related Topics 数组 哈希表
#  👍 909 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# - 时间复杂度：*O(n^2)*，其中 *n* 为数组的长度。枚举子数组开头和结尾需要 *O(n^2)* 的时间，其中求和需要 *O(1)* 的时间复杂度，因此总时间复杂度为 *O(n^2)*。
#
# - 空间复杂度：*O(1)*。只需要常数空间存放若干变量。
# Time Limit Exceeded
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         count = 0
#         for i in range(len(nums)):
#             sum = 0
#             for j in range(i, -1, -1):
#                 sum += nums[j]
#                 if sum == k:
#                     count += 1
#         return count


# 哈希表+前缀和
# pre[i]-pre[i-1] = nums[i]
# pre[i]-pre[j] = k
# pre[j] = pre[i] - k
# 用哈希表记住pre[i]的次数，mp[pre[i]]=mp.get(pre[i], 0)+1
# 如果pre[i]-k在哈希表中出现过，则count应该加上pre[i]-k出现过的次数，即count+=mp.get(pre[i]-k)
# 而pre[i]可以不用记成数组，用pre_sum记就可以

# 时间复杂度：O(N)
# 空间复杂度：O(N)

# 			执行耗时:104 ms,击败了34.98% 的Python3用户
# 			内存消耗:16.9 MB,击败了93.29% 的Python3用户
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp, pre_sum, count = {0: 1}, 0, 0
        for i in nums:
            pre_sum += i
            if pre_sum-k in mp:
                count += mp.get(pre_sum-k)
            mp[pre_sum] = mp.get(pre_sum, 0) + 1
        return count
# leetcode submit region end(Prohibit modification and deletion)
