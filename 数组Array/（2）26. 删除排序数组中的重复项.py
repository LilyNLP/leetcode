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
        
# 总结：
# 1. 不能在for循环的if语句里给j赋值作为初始化，当数组为空时会报错没有初始化，空数组一定要和边界情况一样作为特殊情况考虑，好的编程习惯是在循环外面完成初始化。
# 2. 尽管原数组的重复元素用原数组的指针直接-1比较很好想，也可以尝试思考新指针的特点，比较改变后的数组和原数组。
