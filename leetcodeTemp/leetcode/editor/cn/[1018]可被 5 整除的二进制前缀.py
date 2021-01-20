# 给定由若干 0 和 1 组成的数组 A。我们定义 N_i：从 A[0] 到 A[i] 的第 i 个子数组被解释为一个二进制数（从最高有效位到最低有效位）。 
# 
# 
#  返回布尔值列表 answer，只有当 N_i 可以被 5 整除时，答案 answer[i] 为 true，否则为 false。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[0,1,1]
# 输出：[true,false,false]
# 解释：
# 输入数字为 0, 01, 011；也就是十进制中的 0, 1, 3 。只有第一个数可以被 5 整除，因此 answer[0] 为真。
#  
# 
#  示例 2： 
# 
#  输入：[1,1,1]
# 输出：[false,false,false]
#  
# 
#  示例 3： 
# 
#  输入：[0,1,1,1,1,1]
# 输出：[true,false,false,false,true,false]
#  
# 
#  示例 4： 
# 
#  输入：[1,1,1,0,1]
# 输出：[false,false,false,false,false]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 30000 
#  A[i] 为 0 或 1 
#  
#  Related Topics 数组 
#  👍 99 👎 0

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
# 时间超时
# class Solution:
#     def prefixesDivBy5(self, A: List[int]) -> List[bool]:
#         ans = []
#         for i in range(1, len(A)+1):
#             tmp = A[:i]
#             result = 0
#             for x in range(len(tmp)):
#                 if tmp[x] == 0:
#                     continue
#                 # print(tmp, len(tmp)-1-x)
#                 result += tmp[x]*(2**(len(tmp)-1-x))
#             # print(result)
#             if result % 5 == 0:
#                 ans.append(True)
#             else:
#                 ans.append(False)
#         return ans

# 还是不够快
# class Solution:
#     def prefixesDivBy5(self, A: List[int]) -> List[bool]:
#         ans = []
#         pre = 0
#         for i in A:
#             pre = pre * 2 + i
#             # print(pre)
#             if pre % 5 == 0:
#                 ans.append(True)
#             else:
#                 ans.append(False)
#         # print(ans)
#         return ans


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        ans = []
        pre = 0
        for i in A:
            pre = ((pre << 1) + i) % 5
            ans.append(not pre)
        # print(ans)
        return ans

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    test = Solution()
    print(test.prefixesDivBy5([0]))
    print(test.prefixesDivBy5([1]))
    print(test.prefixesDivBy5([0,1,1]))
    print(test.prefixesDivBy5([1,1,1]))
    print(test.prefixesDivBy5([0,1,1,1,1,1]))
    print(test.prefixesDivBy5([1,1,1,0,1]))
