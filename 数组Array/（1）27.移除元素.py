# 自己的解法：双指针法
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        for k in range(j, len(nums)):
            nums.pop()
        return len(nums)

# 最优解： 双指针法，和自己的解法一样
 
# 延伸问题：如果要删除的元素很少怎么办？
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums) - 1
        while i <= n:
            if nums[i] == val:
                nums[i] = nums[n]
                nums.pop()
                n -= 1
            else:
                i += 1
        return i+1

# 总结：
# 1. 注意题目描述中的细节，“元素顺序可以改变”是解决延伸问题的关键
# 2. 延伸问题的类型：在某种特定情况下如何减少复杂度
# 3. 编程习惯：检查变量初始化；检查数组会不会越界，要注意一首一尾特殊情况下是否正确运行，犯过i<n的错误；数组长度变化时用while
