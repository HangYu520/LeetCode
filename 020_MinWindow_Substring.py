"""
问题: 找到字符串的最小子串, 使得子串包含另一字符串的所有字符

例:
输入: s = "ADOBECODEBANC", t = "ABC"
输出: "BANC" (若没有, 返回空串 "")

条件:
1. s 和 t 都只包含大写和小写字母
2. 1 <= s.length, t.length <= 10^5
"""

class Solution(object):
    """
    思路: (显然采用滑动窗口)
        !  首先有2个问题需要解决:
        1. 如何判断一个子串是否包含t中所有字符 ?
        -- 使用一个哈希表记录 window 中字符出现的次数
        -- 另一个哈希表记录 t 中字符出现的次数
        -- 使用一个整数记录 window 中达到 t 中要求的字符的个数
        -- 若整数的值等于 t 中字符的个数, 则说明 window 中已经包含 t 中所有字符
        2. 如何移动窗口 ?
        -- 不断扩张窗口, 直到 window 中包含 t 中所有字符
        -- 不断缩小窗口, 直到 window 中不再包含 t 中所有字符
        -- 在这个过程中, 记录最小的窗口长度和起始位置
        -- 时间复杂度 : O(n), 空间复杂度 : O(n)
    """
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        window, need = {}, {} # * 记录 window 中字符出现的次数, t 中字符出现的次数
        for c in t: need[c] = need.get(c, 0) + 1 # * 统计 t 中字符出现的次数
        valid = 0 # * 统计 window 中已经满足 t 要求的字符个数 (最终目的 : valid == len(need))
        
        start, min_len = -1, float("inf") # * 最小窗口的起始位置和长度
        left, right = 0, 0 # * 窗口的左右边界

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1 # * 字符添加到 window 中
            if c in need and window[c] == need[c]: # * 若字符 c 满足要求
                valid += 1
            while valid == len(need): # * 缩小窗口
                if right - left + 1 < min_len: # * 更新最小窗口
                    min_len = right - left + 1
                    start = left
                d = s[left]
                left += 1
                window[d] -= 1
                if d in need and window[d] < need[d]: # * 若字符 d 不满足要求
                    valid -= 1
        
        return "" if start == -1 else s[start:start+min_len]

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(f"s = {s}, t = {t}")
    print(f"solution = {Solution().minWindow(s, t)}")   