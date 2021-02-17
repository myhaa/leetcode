# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
#  说明：本题中，我们将空字符串定义为有效的回文串。
#
#  示例 1:
#
#  输入: "A man, a plan, a canal: Panama"
# 输出: true
#
#
#  示例 2:
#
#  输入: "race a car"
# 输出: false
#
#  Related Topics 双指针 字符串
#  👍 329 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [x.lower() for x in s if (x.lower() >= 'a' and x.lower() <= 'z') or (x.lower() >= '0' and x.lower() <= '9')]
        if not s:
            return True
        mid = len(s) // 2
        left = s[:mid]
        right = s[mid:]
        tmp = min(len(left), len(right))
        if left[:tmp] == right[::-1][:tmp]:
            return True
        return False

# leetcode submit region end(Prohibit modification and deletion)
