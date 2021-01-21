# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。 
# 
#  最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。 
# 
#  你可以假设除了整数 0 之外，这个整数不会以零开头。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：digits = [1,2,3]
# 输出：[1,2,4]
# 解释：输入数组表示数字 123。
#  
# 
#  示例 2： 
# 
#  
# 输入：digits = [4,3,2,1]
# 输出：[4,3,2,2]
# 解释：输入数组表示数字 4321。
#  
# 
#  示例 3： 
# 
#  
# 输入：digits = [0]
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= digits.length <= 100 
#  0 <= digits[i] <= 9 
#  
#  Related Topics 数组 
#  👍 613 👎 0

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
# # 自己的解法
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         tmp = ''
#         for i in digits:
#             tmp += str(i)
#         tmp = int(tmp) + 1
#         tmp = [int(x) for x in str(tmp)]
#         x = len(digits) - len(tmp)
#         x = x if x>0 else 0
#         return digits[:x]+tmp

# 看题解的解法
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits
        for i in range(len(digits)-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
        if digits[0] == 0:
            return digits[1:]
        else:
            return digits
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    test = Solution()
    print(test.plusOne([4,3,2,9]))
    print(test.plusOne([0,1]))
    print(test.plusOne([9, 9]))
