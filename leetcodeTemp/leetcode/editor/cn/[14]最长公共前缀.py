# 编写一个函数来查找字符串数组中的最长公共前缀。 
# 
#  如果不存在公共前缀，返回空字符串 ""。 
# 
#  示例 1: 
# 
#  输入: ["flower","flow","flight"]
# 输出: "fl"
#  
# 
#  示例 2: 
# 
#  输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#  
# 
#  说明: 
# 
#  所有输入只包含小写字母 a-z 。 
#  Related Topics 字符串 
#  👍 1402 👎 0

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        elif len(strs) == 1 or len(set(strs)) == 1:
            return strs[0]
        else:
            i = 1
            x_len = 1
            x = []
            y = []
            while x_len == 1:
                y = x
                try:
                    x = list(set([m[:i] for m in strs]))
                except:
                    x = []
                x_len = len(x)
                i += 1
            # print(x, y)
            if len(y) == 1:
                return y[0]
            else:
                return ''
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    # x = ["flower","flow","flight"]
    # x = ["dog","racecar","car"]
    # x = ["","b"]
    x = ["",""]
    test = Solution()
    print(test.longestCommonPrefix(x))
