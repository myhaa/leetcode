# 给定一个整数数组 nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
#
#  示例 1：
#
#  输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# 输出： True
# 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
#
#
#
#  提示：
#
#
#  1 <= k <= len(nums) <= 16
#  0 < nums[i] < 10000
#
#  Related Topics 位运算 记忆化搜索 数组 动态规划 回溯 状态压缩
#  👍 379 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 思路：dfs+剪枝
# 深度优先搜索每个可能的组合， 满足sum(nums)/k的子集
# 		执行耗时:224 ms,击败了26.41% 的Python3用户
# 		内存消耗:14.9 MB,击败了65.23% 的Python3用户
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        nums_sum = sum(nums)  # 求和
        target0 = nums_sum // k  # 求出每个子集应该满足的和
        if max(nums) > target0 or nums_sum % k != 0:  # 如果nums中最大值大于target0，则直接返回false，或者nums_sum对k除不尽
            return False
        state = [False] * len(nums)  # 每个值是否用过
        nums.sort()  # 排序
        return self.dfs(nums, target0, target0, k-1, 0, state)
    
    def dfs(self, nums, target, target0, k, start, state):
        """
        深度优先搜索
        :param target0: 原始target值
        :param nums: 数组
        :param target: 目标值
        :param k: 剩余要找的子集数
        :param start: 开始位置
        :param state: 状态list
        :return:
        """
        if target == 0:  # 如果target=0的话，则找下一组满足子集和为target0的值，start从0开始
            return self.dfs(nums, target0, target0,  k-1, 0, state)
        if k == 0:  # 代表找完
            return True
        for i in range(start, len(nums)):
            if state[i]:
                continue
            state[i] = True
            tmp = self.dfs(nums, target-nums[i], target0, k, i+1, state)
            if tmp:
                return True
            state[i] = False
        return False
# leetcode submit region end(Prohibit modification and deletion)
