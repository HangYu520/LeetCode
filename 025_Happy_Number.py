"""
问题: 判别一个数是否为快乐数
一个快乐数定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1, 也可能是 无限循环 但始终变不到 1。如果可以变为 1, 那么这个数就是快乐数（注: 一定会陷入一个重复的循环, 但不是所有的数都会变为 1)。

例:
输入: 19
输出: true
解释: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

条件:
1. 1 <= n <= 231 - 1
"""

class Solution(object):
    """
    思路:
        首先, 如何取出一个数的每一位数字? 可以通过对10取模和整除10来实现, 或者者将数字转换为字符串, 然后遍历字符串的每个字符并转换回整数.
        A. 哈希表
            1. 创建一个哈希表, 用来存储已经访问过的数字.
            2. 循环判断当前数字是否为1, 如果不是, 则将当前数字的每一位数字的平方和加入到下一个数字中, 并将当前数字更新为下一个数字.
        B. 快慢指针 (龟兔赛跑)
            1. 使用两个指针, 一个快指针每次移动两步, 一个慢指针每次移动一步.
            2. 如果快指针和慢指针相遇, 则说明存在循环, 返回False.
            3. 如果快指针到达1, 则返回True.
    """
    def squareSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        while n > 0:
            digit = n % 10
            total += digit ** 2
            n //= 10
        return total
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if False:
            # 方法A: 哈希表
            seen = set()
            while n != 1:
                n = sum(int(i)**2 for i in str(n))
                if n in seen:
                    return False
                seen.add(n)
            return True
        else:
            # 方法B: 龟兔赛跑
            slow = n
            fast = n
            while True:
                slow = self.squareSum(slow)
                fast = self.squareSum(self.squareSum(fast))
                if slow == fast:
                    break
            return slow == 1

if __name__ == "__main__":
    solution = Solution()
    n = 19
    print(f'n = {n}')
    print(solution.isHappy(n))  # 输出: True