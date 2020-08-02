# 我的解法：j只充当填充的角色
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(len(nums)):
            if  i != 0 and nums[i] != nums[i-1]:
                j += 1
                nums[j] = nums[i]
        return j+1
        
# 官方解法：快指针和慢指针，j既负责填充也负责比较
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(len(nums)):
            if  nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j+1
        
 # 犯错：
 # 1. 不能在if语句里给j赋值作为初始化，当数组为空时会报错，空数组一定要考虑，最保险方式是在循环和if外面就完成初始化。
 
