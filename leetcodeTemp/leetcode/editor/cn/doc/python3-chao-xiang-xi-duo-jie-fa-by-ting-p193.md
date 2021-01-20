# 解法一：二进制+数组+暴力法（超时）
## 思路：
直接判断每个二进制前缀是否被`5`整除。
## 超时代码：
```python3 []
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        return [not int("".join(map(str, A[:i])), 2)%5 for i in range(1, len(A)+1)]
```
# 解法二：二进制+数组+暴力法优化（通过）
## 思路：
判断每个二进制前缀是否被`5`整除，用变量保存当前二进制前缀。
## 通过代码一：（这个思路速度很慢，超过20%）
```python3 []
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        a = ""
        res = []
        for i in A:
            a += str(i)
            res.append(not int(a, 2)%5)
        return res
```
# 解法三：二进制+数组+位运算（通过）
## 思路：
利用变量保存当前二进制前缀的值，每次判断是否被`5`整除，并改变保存当前二进制前缀的值的变量。
### 二进制增加：
###### 先将前面的数乘`2`，再加上新增数。
## 通过代码二：（这个思路速度还不错，超过70%）
```python3 []
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        pre = 0
        for i in A:
            pre = (pre<<1)+i
            res.append(not pre%5)
        return res
```
# 解法四：二进制+数组+位运算优化（通过）
## 思路：
利用变量保存当前二进制前缀的值，每次判断是否被5整除，改变保存当前二进制前缀的值的变量并对5取余。
### 二进制增加：
###### 先将前面的数乘`2`，再加上新增数。
### 取余原因：
###### 因为`n*2%5 == n%5*2%5`，所以取余，这样就不用保存非常大的数了。
## 通过代码三：（这个思路速度很快，超过97.5%）
```python3 []
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        pre = 0
        for i in A:
            pre = ((pre<<1)+i)%5
            res.append(not pre)
        return res
```