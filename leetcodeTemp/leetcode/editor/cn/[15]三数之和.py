# date: 2021-03-15 22:16:36

# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重
# 复的三元组。
#
#  注意：答案中不可以包含重复的三元组。
#
#
#
#  示例 1：
#
#
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#
#
#  示例 2：
#
#
# 输入：nums = []
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：nums = [0]
# 输出：[]
#
#
#
#
#  提示：
#
#
#  0 <= nums.length <= 3000
#  -105 <= nums[i] <= 105
#
#  Related Topics 数组 双指针
#  👍 3090 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 解法：分成三个指针，i, p, q
# * 第一层循环就用0-nums[i]，
# * 然后对得到的target值，在nums[i+1:]上用双指针p,q找出对应解
# * 值得注意的事，i>0 and nums[i] == nums[i-1]的 且p>i+1 and nums[p] == nums[p-1]的不考虑，避免重复
# 时间复杂度：O(N^2)
class Solution:
    def search(self, x, nums):
        p, q, res = 0, len(nums)-1, []
        target = 0 - x
        while p < q:
            if p > 0 and nums[p] == nums[p-1]:
                p += 1
                continue
            tmp = nums[p] + nums[q]
            if tmp == target:
                res.append([x, nums[p], nums[q]])
                p += 1
                q -= 1
            elif tmp < target:
                p += 1
            else:
                q -= 1
        return res
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            tmp1 = self.search(nums[i], nums[i+1:])
            if tmp1:
                res.extend(tmp1)
        return res
        
# leetcode submit region end(Prohibit modification and deletion)
