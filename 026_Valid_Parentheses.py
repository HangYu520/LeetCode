"""
问题: 判断给定的字符串是否为有效的括号组合

例:
输入: s = "([)]"
输出: false

条件:
1. 1 <= s.length <= 10^4
2. s 仅由括号 '()[]{}' 组成
"""

class Solution(object):
    """
    思路:
        经典的栈问题
        1. 遇到左括号, 则将其压入栈中
        2. 遇到右括号, 则判断栈顶的左括号是否匹配, 若匹配则弹出栈顶元素, 否则返回 False
        3. 遍历结束后, 栈中若有元素, 则返回 False, 否则返回 True
    """
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {'(':')', '[':']', '{':'}'}

        for brack in s:
            if brack in pairs:
                stack.append(brack)
            elif stack and pairs[stack[-1]] == brack:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0

if __name__ == "__main__":
    s = "([)]"
    print(f's={s}')
    print(f'{Solution().isValid(s)}')