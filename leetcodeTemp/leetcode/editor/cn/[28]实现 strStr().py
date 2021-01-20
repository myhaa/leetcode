# 实现 strStr() 函数。 
# 
#  给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如
# 果不存在，则返回 -1。 
# 
#  示例 1: 
# 
#  输入: haystack = "hello", needle = "ll"
# 输出: 2
#  
# 
#  示例 2: 
# 
#  输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
#  
# 
#  说明: 
# 
#  当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。 
# 
#  对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。 
#  Related Topics 双指针 字符串 
#  👍 669 👎 0

################################################
# 解法一：最直接的方法 - 沿着字符换逐步移动滑动窗口，将窗口内的子串与 needle 字符串比较。
################################################


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_haystack, len_needle = len(haystack), len(needle)
        if len_needle == 0:
            return 0
        for i in range(len_haystack-len_needle+1):
            # print(haystack, needle, haystack[i:i+len_needle])
            if haystack[i] != needle[0]:
                continue
            if haystack[i:i+len_needle] == needle:
                return i
        return -1
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    test = Solution()
    haystack = "aaaaa"
    needle = "bba"
    print(test.strStr(haystack, needle))
    haystack = "hello"
    needle = "ll"
    print(test.strStr(haystack, needle))
    haystack = "a"
    needle = "a"
    print(test.strStr(haystack, needle))
    haystack = "abc"
    needle = "c"
    print(test.strStr(haystack, needle))


