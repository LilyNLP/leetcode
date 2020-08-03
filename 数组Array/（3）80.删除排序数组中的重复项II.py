# 我的解法：
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        k = 0
        for i in range(len(nums)):
            if i == 0:
                continue
            if nums[i] != nums[i-1]:
                k = 0
            if nums[i] == nums[i-1]:
                k += 1
            if k < 2:
                j += 1
            nums[j] = nums[i]
        return j+1
        
        
  # 最优解：
  
