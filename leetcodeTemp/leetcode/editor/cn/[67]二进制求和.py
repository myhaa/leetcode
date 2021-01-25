# 给你两个二进制字符串，返回它们的和（用二进制表示）。 
# 
#  输入为 非空 字符串且只包含数字 1 和 0。 
# 
#  
# 
#  示例 1: 
# 
#  输入: a = "11", b = "1"
# 输出: "100" 
# 
#  示例 2: 
# 
#  输入: a = "1010", b = "1011"
# 输出: "10101" 
# 
#  
# 
#  提示： 
# 
#  
#  每个字符串仅由字符 '0' 或 '1' 组成。 
#  1 <= a.length, b.length <= 10^4 
#  字符串如果不是 "0" ，就都不含前导零。 
#  
#  Related Topics 数学 字符串 
#  👍 546 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 自己写的
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         len_a = len(a)
#         len_b = len(b)
#         tmp = abs(len_a-len_b)+1
#         if len_a < len_b:
#             a = tmp*'0' + a
#             b = '0' + b
#         elif len_a > len_b:
#             a = '0' + a
#             b = tmp*'0' + b
#         else:
#             a = '0' + a
#             b = '0' + b
#
#         result = [0] * len(a)
#         # print(a,b,result)
#         for i in range(len(result)-1, 0, -1):
#             tmp = int(a[i]) + int(b[i]) + result[i]
#             if tmp < 2:
#                 result[i] = tmp
#             elif tmp == 2:
#                 result[i] = 0
#                 result[i-1] = 1
#             else:
#                 result[i] = 1
#                 result[i-1] = 1
#         if result[0] == 0:
#             result = result[1:]
#         tmp = ''
#         for x in result:
#             tmp+= str(x)
#         return tmp
# python特性
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return '{0:b}'.format(int(a,2)+int(b,2))

# leetcode submit region end(Prohibit modification and deletion)



if __name__ == "__main__":
    test = Solution()
    print(test.addBinary(a = "1010", b = "1011"))
    print(test.addBinary(a = "111", b = "1"))
    print(test.addBinary(a="11", b="1"))
    print(test.addBinary(a="1", b="111"))
    print(test.addBinary(a="1111", b="1111"))
