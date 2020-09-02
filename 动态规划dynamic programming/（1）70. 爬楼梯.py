# 我的解法：动态规划，时间复杂度n，空间复杂度n
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n)]
        if n < 3:
            return n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]
# 总结：
# 1. python语言上：常见数组全零初始化方式； range(start包括, stop不包括, step)。
# 2. 动态规划的要点：定义什么是状态，定义状态转移方程，定义边界条件。
        
# 官方解法1：动态规划+滚动数组，节省空间复杂度为1
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b, c = 0, 0, 1
        for i in range(n):
            a, b = b, c
            c = a + b
        return c
# 总结：滚动数组思想对于类似f[i] = f[i-1] + f[i-2]之类的线性递推都可以起到节省空间的作用。
        
# 官方解法2： 矩阵快速幂
# 线性代数！数列的递推关系（齐次线性递推，部分非齐次也可换元法转化为齐次） -> 矩阵的递推关系
# 快速幂如何实现？

# 官方解法3：用斐波那契数列的通项公式

