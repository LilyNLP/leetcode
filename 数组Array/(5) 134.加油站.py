# 我的解法：
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for StartP in range(n):
            j = StartP
            GasAmount = 0
            while j != n + StartP:
                GasAmount = GasAmount + gas[j%n] - cost[j%n]
                if GasAmount >= 0:
                    j += 1
                else:
                    break
            if j  == n + StartP:
                return StartP
        return -1
    
 # 
