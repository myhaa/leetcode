# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
#
#
#  进阶：你可以设计并实现时间复杂度为 O(n) 的解决方案吗？
#
#
#
#  示例 1：
#
#
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
#
#  示例 2：
#
#
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
#
#
#
#
#  提示：
#
#
#  0 <= nums.length <= 104
#  -109 <= nums[i] <= 109
#
#  Related Topics 并查集 数组
#  👍 785 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

# 排序
# 思路：使用python自带排序算法排序，再使用动态规划判断最大连续数组长度
# 时间复杂度：O(nlogn)
# 空间复杂度：O(N)
# 			执行耗时:84 ms,击败了23.05% 的Python3用户
# 			内存消耗:22.6 MB,击败了13.47% 的Python3用户

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if len(nums) <= 1:
#             return len(nums)
#         nums.sort()
#         dp = [1] * len(nums)
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i-1]+1:
#                 dp[i] = dp[i-1] + 1
#             elif nums[i] == nums[i-1]:
#                 dp[i] = dp[i-1]
#         # print(nums, dp)
#         return max(dp)

# 哈希表
# 思路：将nums去重为哈希表，对表中每一个元素x判断x+1,x+2,x+3,...,x+y是否在表终，如果成立，则长度为y+1
# 可以把x-1存在在表中的x可以不用判断，因为x-1作为起点的序列肯定比x起点的序列长
# 时间复杂度：O(N)
# 空间复杂度：O(N)
# 			执行耗时:68 ms,击败了29.77% 的Python3用户
# 			内存消耗:26 MB,击败了7.11% 的Python3用户
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         ans = 0  # 最终答案
#         nums_set = set(nums)  # 去重
#         for i in nums_set:  # 遍历每个元素
#             if i - 1 not in nums_set:  # 用哈希表判断是否存在，时间复杂度为O(1)
#                 cur = 1  # 以i为起点的连续序列长度
#                 x = i  # x + 1
#
#                 while x + 1 in nums_set:  # 一直累加判断是否在set
#                     x += 1
#                     cur += 1
#                 ans = max(ans, cur)
#         return ans


# 并查集
# 思路：将列表弄成并查集，并查集拥有合并，查找功能
# 时间复杂度：O(N)
# 空间复杂度：O(N)
# 		执行耗时:304 ms,击败了15.05% 的Python3用户
# 		内存消耗:29.5 MB,击败了5.04% 的Python3用户
class UnionFind():
    def __init__(self, arr):
        self.parent = {}
        for i in arr:
            self.parent[i] = i  # 各自为战
    
    def union(self, p, q):
        """
        将p和q合并
        :param p:
        :param q:
        :return:
        """
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
        if root_p is None or root_q is None:
            return
        if root_p < root_q:
            self.parent[root_p] = root_q
        else:
            self.parent[root_q] = root_p
    
    def find(self, p):
        """
        找到p的头结点
        :param p:
        :return:
        """
        if p not in self.parent:
            return
        root_p = self.parent[p]
        if root_p == p:
            return p
        else:
            self.parent[p] = self.find(root_p)  # 路径压缩，每个结点的父节点都设为根节点
            return self.parent[p]


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        un = UnionFind(nums)  # init
        for i in nums:
            un.union(i, i+1)  # 将i和i+1合并
        ans = 1
        for i in nums:
            ans = max(ans, un.find(i)-i+1)  # 找到最大路径
        return ans
# leetcode submit region end(Prohibit modification and deletion)
