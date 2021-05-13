# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
#
#  在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表
# 示如果要学习课程 ai 则 必须 先学习课程 bi 。
#
#
#  例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
#
#
#  请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
#
#
#
#  示例 1：
#
#
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：true
# 解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
#
#  示例 2：
#
#
# 输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
# 输出：false
# 解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
#
#
#
#  提示：
#
#
#  1 <= numCourses <= 105
#  0 <= prerequisites.length <= 5000
#  prerequisites[i].length == 2
#  0 <= ai, bi < numCourses
#  prerequisites[i] 中的所有课程对 互不相同
#
#  Related Topics 深度优先搜索 广度优先搜索 图 拓扑排序
#  👍 804 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

# 拓扑排序

# 时间复杂度: O(n+m)，其中 n 为课程数，m 为先修课程的要求数。这其实就是对图进行深度优先搜索的时间复杂度。
#
# 空间复杂度: O(n+m)。题目中是以列表形式给出的先修课程关系，为了对图进行深度优先搜索，我们需要存储成邻接表的形式，空间复杂度为 O(n+m)。在深度优先搜索的过程中，我们需要最多 O(n)
# 的栈空间（递归）进行深度优先搜索，因此总空间复杂度为 O(n+m)。

# 			执行耗时:44 ms,击败了88.39% 的Python3用户
# 			内存消耗:17.6 MB,击败了20.23% 的Python3用户

import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        result = list()
        visited = [0] * numCourses
        valid = True
        
        for u, v in prerequisites:
            edges[v].append(u)
        
        def dfs(u):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] = 2
            result.append(u)
        
        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)
        
        return valid
# leetcode submit region end(Prohibit modification and deletion)
