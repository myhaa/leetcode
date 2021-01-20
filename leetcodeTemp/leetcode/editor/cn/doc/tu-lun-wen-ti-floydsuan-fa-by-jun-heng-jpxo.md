这道题可以转化为一个 带权图问题。
a/b = 2, b/c=3 => a/c=6
可以抽象为 a到b的边权重为2，b到c的边权重为3， a到c的边权重为2*3=6，
图中任意2点的距离用2点之间边的权重乘积表示.
如此，问题归为，如何求图中任意两点的距离。
可以使用Floyd算法解决。
```python
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict
        graph = defaultdict(int)
        set1 = set()
        for i in range(len(equations)):
            a, b = equations[i]
            graph[(a, b)] = values[i]
            graph[(b, a)] = 1/values[i]
            set1.add(a)
            set1.add(b)

        # Floyd算法 求图中任意2点距离
        arr = list(set1)
        for k in arr:
            for i in arr:
                for j in arr:
                    if graph[(i, k)] and graph[(k, j)]:
                        graph[(i, j)] = graph[(i, k)] * graph[(k, j)]
        
        res = []
        for x, y in queries:
            if graph[(x, y)]:
                res.append(graph[(x, y)])
            else:
                res.append(-1)
        return res
```
