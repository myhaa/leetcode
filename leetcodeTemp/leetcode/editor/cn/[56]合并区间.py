# date: 2021-03-28 23:05:20

# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返
# 回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
#
#
#
#  示例 1：
#
#
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
#
#  示例 2：
#
#
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
#
#
#
#  提示：
#
#
#  1 <= intervals.length <= 104
#  intervals[i].length == 2
#  0 <= starti <= endi <= 104
#
#  Related Topics 排序 数组
#  👍 868 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 时间复杂度：O(nlogn)
# 空间复杂度：O(N)
# 执行耗时:32 ms,击败了99.61% 的Python3用户
# 内存消耗:15.6 MB,击败了25.22% 的Python3用户
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        tmp = sorted(intervals, key=lambda x: x[0])
        res = [tmp[0]]
        for i in range(1, len(tmp)):
            if res[-1][1] >= tmp[i][1] >= tmp[i][0]:
                continue
            elif res[-1][1] >= tmp[i][0]:
                res[-1] = [res[-1][0], tmp[i][1]]
            else:
                res.append(tmp[i])
        return res
# leetcode submit region end(Prohibit modification and deletion)
