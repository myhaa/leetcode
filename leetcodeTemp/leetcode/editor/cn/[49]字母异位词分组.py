# date: 2021-03-26 23:05:48

# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
#  示例:
#
#  输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
#
#  说明：
#
#
#  所有输入均为小写字母。
#  不考虑答案输出的顺序。
#
#  Related Topics 哈希表 字符串
#  👍 695 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 时间复杂度：O(nlogn)
# 执行耗时:44 ms,击败了98.82% 的Python3用户
# 内存消耗:17.4 MB,击败了90.44% 的Python3用户
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for x in strs:
            tmp = ''.join(sorted(x))
            if tmp not in res:
                res[tmp] = [x]
            else:
                res[tmp].append(x)
        return list(res.values())
        
# leetcode submit region end(Prohibit modification and deletion)
