参考作者：max-LFszNScOfE
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/shuang-zhi-zhen-shan-chu-zhong-fu-xiang-dai-you-hu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

里面讲的双指针很清晰了，这里用python模仿写了一段。
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 双指针做法
        # 若p和q位置元素相等，则q向后移动一位
        # 若p和q位置元素不等，则p+1位置元素替换为q位置元素，且p，q均向后移动一位
        # 循环之后q=数组长度
        # 返回前p+1个位置元素
        p, q = 0, 1
        while(q<len(nums)):
            if nums[p] == nums[q]:
                q = q + 1
            else:
                nums[p+1] = nums[q]
                p = p + 1
                q = q + 1
        return len(nums[0:p+1]) 

![1608459541(1).png](https://pic.leetcode-cn.com/1608459574-gCHwaT-1608459541\(1\).png)

速度倒是很快，但内存消耗挺大的。