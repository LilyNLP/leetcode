# 我的解法：
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 0<nums[i]<len(nums)+1 and nums[i] != nums[nums[i]-1]:
                k = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = k
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
        
# 官方解法1（最优解：置换）：
 class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
        
# 官方解法2（打标记）：想法上更清晰简单，直接常数个for，不需要for里套while
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])
        
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        return n + 1
        
# 复杂度分析：
# 时间复杂度：O(N)，= N + N。

# 算法知识点：
# 1. 哈希表的意义是通过空间复杂度换时间复杂度，本来是1空间到N空间里遍历查找（或二分查找等），时间复杂度是O(N^2)或O(NlogN)，用了哈希表之后是将原来的N空间用哈希函数映射到新增的N空间，然后用哈希函数将查找变成直接定位，时间复杂度变成O(N)。
# 2. 哈希表和数组有相似的地方。本题用到的方法相当于创建了一个哈希函数为f(key) = key - 1的哈希表，即一个array[i] = i + 1的数组，这样可以实现数组的原地更改，将原哈希表会新增N空间的弊端抹去，转而通过置换或者打标记的方法增加一些并达不到O(N^2)复杂度的操作来实现0额外空间。
# 3. 注意当要求时间复杂度为O(N)时，可以考虑多个N的循环，也可以考虑在一个N的循环里套while循环，最终只需要看执行语句是不是执行了O(N)次，而不是看条件语句的框架。
# 4. 在遍历同时交换，当在该位置交换之后继续考虑当前位置的时候while的使用。

# python知识点：
# 1. python中的数组两个位置的数的交换可以直接 A, B = B, A。
# 2. python中可以直接用1<i<n来表示区间。
