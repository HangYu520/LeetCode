"""
问题: 找到所有字符串中的最长公共前缀

例:
输入: ["flower","flow","flight"]
输出: "fl"

条件:
1. 1 <= strs.length <= 200
2. 0 <= strs[i].length <= 200
3. strs[i] 仅由小写英文字母组成
"""

class Solution(object):
    """
    思路:
        A. 逐个比较
        1. 定义辅助函数 longestPrefix 比较两个字符串的公共前缀
        2. 逐个比较 strs 中的字符串，更新最长公共前缀
        -- m 为字符串平均长度, n 为字符串数量
        -- 逐个添加比较, 时间复杂度: O(mn)
        -- 切片比较, 时间复杂度: O(n)
    """
    def longestPrefix(self, str1, str2):
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        
        if False: # 引入 prefix 逐个添加 O(m)
            prefix = ""
            for i in range(len(str1)):
                if str1[i] == str2[i]:
                    prefix += str1[i]
                else:
                    break
            return prefix
        else: # 直接切片 O(1)
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    return str1[:i]
            return str1
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_prefix = strs[0]
        for i in range(1, len(strs)):
            common_prefix = self.longestPrefix(common_prefix, strs[i])
            if common_prefix == "": break
        return common_prefix

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    print(f'strs = {strs}')
    print(f'solution = {Solution().longestCommonPrefix(strs)}')