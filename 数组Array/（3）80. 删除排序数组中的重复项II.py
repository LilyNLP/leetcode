# 我的解法：和前一题一样的双指针，用一个计数器来更新重复次数，这样每次只和前一个比较，避免每次和上上个比较的时候上上个已经被更新的问题
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        k = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                k = 0
            else:
                k += 1
            if k < 2:
                j += 1
            nums[j] = nums[i]
        return j+1
        
        
# 官方解法：
# 解法1：直接删除
class Solution(object):
    def removeDuplicates(self, nums):
        i, count = 1, 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                count += 1
                if count > 2:
                    nums.pop(i)
                    i-= 1    
            else:
                count = 1
            i += 1                   
        return len(nums)
# 复杂度分析：时间复杂度 = N+N^2 = O(N^2)，空间复杂度O(1)

# 解法2：和我的解法一样的覆盖法，时间复杂度 = O(N)

# 总结：
# 1. python：赋值时候可以多个变量写在一行赋值，for 循环里 continue可以直接跳到下一个循环
# 2. 删除和覆盖相比，删除需要O(N)的复杂度，尽量避免，如果要删除因为数组长度在变记得要把for循环改为while循环，指针也要--
  
