# 实现 int sqrt(int x) 函数。 
# 
#  计算并返回 x 的平方根，其中 x 是非负整数。 
# 
#  由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。 
# 
#  示例 1: 
# 
#  输入: 4
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
#      由于返回类型是整数，小数部分将被舍去。
#  
#  Related Topics 数学 二分查找 
#  👍 577 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 自己写的
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x <= 1:
#             return x
#         for i in range(1, x//2+1):
#             if i*i <= x and (i+1)*(i+1)>x:
#                 return i

# 二分查找
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l+r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

# leetcode submit region end(Prohibit modification and deletion)


test = Solution()
print(test.mySqrt(0))
print(test.mySqrt(1))
print(test.mySqrt(2))
print(test.mySqrt(4))
print(test.mySqrt(5))
print(test.mySqrt(6))
print(test.mySqrt(7))
print(test.mySqrt(8))
print(test.mySqrt(9))
print(test.mySqrt(17))
