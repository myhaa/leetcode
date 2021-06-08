# 请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。
#
#
#  例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2
# , 1, 1, 0, 0]。
#
#  提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
#  Related Topics 栈 哈希表
#  👍 772 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 暴力解法
# 等待结果超时
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         if len(temperatures) <= 1:
#             return [0]
#         p = 0
#         res = []
#         while p < len(temperatures):
#             res.append(0)
#             q = p + 1
#             while q < len(temperatures):
#                 if temperatures[q] > temperatures[p]:
#                     res[p] = q - p
#                     break
#                 q += 1
#             p += 1
#         # print(res)
#         return res

# 栈
# 将下标入栈，形成单调栈
# 时间复杂度：O(N)
# 空间复杂度：O(N)
# 			执行耗时:212 ms,击败了83.25% 的Python3用户
# 			内存消耗:20.2 MB,击败了7.36% 的Python3用户
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         if len(temperatures) <= 1:
#             return [0]
#         stack = []
#         res = [0] * len(temperatures)
#         for index, value in enumerate(temperatures):
#             if not stack:
#                 stack.append(index)
#                 continue
#             while stack and value > temperatures[stack[-1]]:
#                 x = stack.pop()
#                 res[x] = index - x
#             else:
#                 stack.append(index)
#         return res

# 哈希表
# 时间复杂度：O(NM)
# 空间复杂度：O(M)
# 		执行耗时:2360 ms,击败了5.00% 的Python3用户
# 		内存消耗:19.4 MB,击败了22.62% 的Python3用户

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans, nxt, big = [0]*n, dict(), 1e8
        for i in range(n-1, -1, -1):
            warm_index = min([nxt.get(x, big) for x in range(temperatures[i]+1, 102)])
            if warm_index != big:
                ans[i] = warm_index - i
            nxt[temperatures[i]] = i
        return ans
        
# leetcode submit region end(Prohibit modification and deletion)
