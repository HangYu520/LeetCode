"""
问题: 字符串异位词分组
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["ate","eat","tea"], ["nat","tan"], ["bat"]]

条件:
1. 1 <= strs.length <= 104
2. 0 <= strs[i].length <= 100
3. strs[i] 只包含小写字母
"""

class Solution(object):
    """
    思路:
        判断两个词是不是异位词很简单, 这里的关键是如何分组, 如何只是简单的遍历, 那时间复杂度会很高. 因此我们应该利用哈希表来存储分组信息. 具体做法是:
        1. 遍历每个字符串, 提取出字符串的元组作为键
        2. 使用这个元组作为哈希表的键, 将原字符串添加到对应的值列表中.
        3. 最后返回哈希表中的所有值列表.
        -- 时间复杂度: O(NK), 空间复杂度: O(NK)
    """
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = {}

        for s in strs:
            letters = [0] * 26
            for char in s:
                letters[ord(char) - ord('a')] += 1
            key = tuple(letters) # 转换为元组以便作为哈希表的键
            if key not in group:
                group[key] = []
            group[key].append(s)
        
        return list(group.values())

if __name__ == "__main__":
    lists = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Input = {lists}")
    solution = Solution()
    result = solution.groupAnagrams(lists)
    print(f"Output = {result}")