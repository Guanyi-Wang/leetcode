class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        Generate a factorial lookup table
        """

        def factorial(n):
            fac = [1]
            f = 1
            for i in range(1, n + 1):
                f = f * i
                fac.append(f)
            return fac

        fac = factorial(n)
        ans = ''
        index = []
        nums = [i for i in range(1, n + 1)]
        k = k - 1
        for i in range(n - 1, -1, -1):  # from n-1 to 0
            index.append(k // fac[i])
            k %= fac[i]
        print(index)
        print(nums)
        for i in index:
            ans += str(nums.pop(i))
        return ans

