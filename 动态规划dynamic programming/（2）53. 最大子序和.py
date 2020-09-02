# 我的解法：动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]
        return max(dp)
# 总结：
# 1. 这题的关键在于“连续”，它决定了我们定义动归状态和状态转移方程的方式。同时这题并不是以最终状态为解答，而是多一步max。
# 2. python语言：max(array, key = funct x: abs(x))

# 官方解法1：动态规划 + 滚动数组
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a = nums[0]
        b = nums[0]
        for i in range(1, len(nums)):
            if a < 0:
                a = nums[i]
            else:
                a = a + nums[i]
            if a > b:
                b = a
        return b
        
# 这个写法虽然简洁但实际跑出来更慢        
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a, b = nums[0], nums[0]
        for i in range(1, len(nums)):
            a = max(nums[i] + a, nums[i])
            b = max(a, b)
        return b

# 官方解法2：分治法
# 二刷时候再补上
