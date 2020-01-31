class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        output = []

        #用list存储从1到n的阶乘
        factorial = [1]*n
        for i in range(1, n):
            factorial[i] = factorial[i-1] * (i+1)
        
        # n = 1 单独考虑
        if n == 1:
            return "1"

        rec = [0]*n
        r = k
        for i in range(n-1):
            q = int(r / factorial[n-2-i]) + 1
            r = r % factorial[n-2-i]
            if r == 0:
                q -= 1 
                r = factorial[n-2-i]
            j = 0
            while 1:
                if j >= q:
                    break
                if rec[j] == 1:
                    q += 1
                j += 1
            output.append(str(q))
            rec[q-1] = 1
        
        # 最后一位单独考虑
        for i in range(n):
            if rec[i] == 0:
                output.append(str(i+1))

        return ''.join(output)
