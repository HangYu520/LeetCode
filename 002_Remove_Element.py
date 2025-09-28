"""
问题: 原地删除数组中指定元素, 并重排原数组保持前面为非删除项, 返回非删除项个数。

例：
输入: 
nums = [3,2,2,3], val = 3

输出: 
2, nums = [2,2,_,_]

条件:
1. 0<= nums.length <=100
2. 0<= nums[i] <=50
3. 0<= val <=100
"""

class Solution(object):
    """
    思路:
        
        1. 创建两个指针, 一个指向当前非删除项, 一个指向当前项。
        2. 遍历数组, 如果当前项等于val, 则将当前项与后面项交换, 并将当前项后移一位。
        -- 时间复杂度: O(n), 空间复杂度: O(1)
        -- 注意: 删除项后, 数组长度不变, 只需返回非删除项个数。
    """
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # [3,2,2,3]
        #  ^     ^
        #  i     j
        n = len(nums)
        i, j = 0, n-1

        while j >= i:
            # j 需要删除
            if nums[j] == val:
                nums[j] = -1
                j -= 1
            else:
                # i 需要删除
                if nums[i] == val:
                    nums[i] = nums[j]
                    nums[j] = -1
                    j -= 1
                # i 不需要删除
                i += 1
        
        return j+1
    
if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(f'nums={nums}')
    print(f'val={val}')
    k = Solution().removeElement(nums, val)
    print(f'solution={k},{nums}')