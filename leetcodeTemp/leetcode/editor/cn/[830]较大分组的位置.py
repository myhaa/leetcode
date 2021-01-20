# 在一个由小写字母构成的字符串 s 中，包含由一些连续的相同字符所构成的分组。 
# 
#  例如，在字符串 s = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。 
# 
#  分组可以用区间 [start, end] 表示，其中 start 和 end 分别表示该分组的起始和终止位置的下标。上例中的 "xxxx" 分组用区间表示
# 为 [3,6] 。 
# 
#  我们称所有包含大于或等于三个连续字符的分组为 较大分组 。 
# 
#  找到每一个 较大分组 的区间，按起始位置下标递增顺序排序后，返回结果。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abbxxxxzzy"
# 输出：[[3,6]]
# 解释："xxxx" 是一个起始于 3 且终止于 6 的较大分组。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "abc"
# 输出：[]
# 解释："a","b" 和 "c" 均不是符合要求的较大分组。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "abcdddeeeeaabbbcd"
# 输出：[[3,5],[6,9],[12,14]]
# 解释：较大分组为 "ddd", "eeee" 和 "bbb" 
# 
#  示例 4： 
# 
#  
# 输入：s = "aba"
# 输出：[]
#  
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 仅含小写英文字母 
#  
#  Related Topics 数组 
#  👍 93 👎 0

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        s = list(s)
        sLen = len(s)
        if sLen < 3:
            return []
        result = []  # 结果
        start = 0
        end = 0
        stack = [s[0]]  # 栈
        for i in range(1, sLen):
            if stack[0] == s[i]:
                end += 1
                if i == sLen - 1 and sLen-1-start >= 2:
                    result.append([start, sLen - 1])
                else:
                    continue

            else:
                if end - start >= 2:
                    result.append([start, end])
                stack.pop(0)
                stack.append(s[i])
                start = i
                end = i
        return result
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    test = Solution()
    print(test.largeGroupPositions('abbxxxxzzy'))
    print(test.largeGroupPositions('aba'))
    print(test.largeGroupPositions('aaa'))
    print(test.largeGroupPositions('bababbabaa'))
    print(test.largeGroupPositions('abcdddeeeeaabbbcd'))