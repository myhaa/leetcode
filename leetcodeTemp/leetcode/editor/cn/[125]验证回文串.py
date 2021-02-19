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
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = [x.lower() for x in s if (x.lower() >= 'a' and x.lower() <= 'z') or (x.lower() >= '0' and x.lower() <= '9')]
#         if not s:
#             return True
#         mid = len(s) // 2
#         left = s[:mid]
#         right = s[mid:]
#         tmp = min(len(left), len(right))
#         if left[:tmp] == right[::-1][:tmp]:
#             return True
#         return False

# 双指针
class Solution:
	def isPalindrome(self, s: str) -> bool:
		s = [x.lower() for x in s if (x.lower() >= 'a' and x.lower() <= 'z') or (x.lower() >= '0' and x.lower() <= '9')]
		if not s:
			return True
		left, right = 0, len(s)-1
		while left < right:
			# while left<right and ~((s[left].lower() >= 'a' and s[left].lower() <= 'z') or (s[left].lower() >= '0' and s[left].lower() <= '9')):
			# 	left += 1
			# while right>0 and ~((s[right].lower() >= 'a' and s[right].lower() <= 'z') or (s[right].lower() >= '0' and s[right].lower() <= '9')):
			# 	right -= 1
			if s[left] != s[right]:
				return False
			left, right = left+1, right-1
		return True

# leetcode submit region end(Prohibit modification and deletion)
