"""
问题: 给定一个单词数组和一个长度maxWidth, 输出一个格式化后的文本

例：
输入: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

要求：
1. 使得每行恰好有 maxWidth 个字符并且完全（左和右）对齐
2. 采用贪婪的方法来打包单词；也就是说，在每一行中尽可能多地打包单词
3. 单词之间的额外空格应尽可能均匀分布，若不能均匀分布，则左侧将比右侧分配更多的空格
5. 对于最后一行文本，应左对齐，并且单词之间不插入额外的空格

条件：
1. 1 <= words.length <= 300
2. 1 <= words[i].length <= 20
3. words[i] 由小写英文字母组成
4. 1 <= maxWidth <= 100
5. words[i].length <= maxWidth
"""

class Solution:
    """
    思路：
        按照题设使用贪心算法，考虑所有的情况
        1. 确定每行的单词
        -- 从左到右遍历单词，用贪心策略尽可能多放单词
        -- 计算当前行已选单词的总长度 + 最小空格数 ≤ maxWidth
        -- 最小空格数 = (单词数 - 1), 因为每个间隔至少1个空格
        2. 处理非最后一行
        -- 对于非最后一行，需要两端对齐：
        -- 计算需要分配的总空格数: totalSpaces = maxWidth - 所有单词长度和
        -- 计算平均每个间隔的空格数: baseSpaces = totalSpaces / (单词数-1)
        -- 计算多余的空格数: extraSpaces = totalSpaces % (单词数-1)
        3. 处理最后一行
        -- 左对齐, 单词间只加1个空格
        -- 剩余部分用空格填充到行末
        -- 时间复杂度: O(n), 空间复杂度: O(n)
    """
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = [] # 最终结果
        i = 0 # 迭代索引

        while i < len(words):
            # 主循环，构造每一行的单词和空格
            line_words = [] # 当前行已选的单词
            line_length = 0 # 当前行已选单词的总长度

            # 贪心策略：尽可能多地选择单词
            while i < len(words) and (line_length + len(words[i])) + len(line_words) <= maxWidth:
            #                       (单   词   的   长   度   和) + (最  小  空  格  数)    
                line_words.append(words[i])
                line_length += len(words[i])
                i += 1

            line = '' # 当前行的排版结果

            if i == len(words) or len(line_words) == 1:
                # 当前为最后一行 or 只有一个单词 ： 执行左对齐
                line = ' '.join(line_words)
                line += ' '*(maxWidth - len(line)) # 补全剩下的空格
            else:
                # 非最后一行且不止一个单词 : 执行左右两边对齐
                totalSpace = maxWidth - line_length # 总的空格数
                baseSpace = totalSpace // (len(line_words) - 1) # 均匀分布的空格数
                extraSpace = totalSpace % (len(line_words) - 1) # 多余的空格数

                line = line_words[0]
                for j in range(1, len(line_words)):
                    line += ' '*baseSpace # 补上固定的空格数
                    line += ' '*(1 if j <= extraSpace else 0) # 前几个单词补上多余的空格数
                    line += line_words[j]
            
            res.append(line) # 存入当前行的结果
        
        return res

if __name__ == '__main__':
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxint = 16
    solution = Solution().fullJustify(words, maxint)
    print(f'words = {words}')
    print('solution = ', end='')
    for i in range(len(solution)):
        if i == 0:
            print(solution[i])
        else:
            print(f'           {solution[i]}')