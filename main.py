def fib(n, dic={}):
    if n in dic:
        return dic[n]

    if n <= 2:
        return 1

    dic[n] = fib(n - 1) + fib(n - 2)
    return dic[n]


def gridTraveler(m, n, memo={}):
    key = str(m) + ',' + str(n)


    if (key) in memo:
        return memo[key]

    if m == 0 or n == 0:
        return 0

    if m == 1 and n == 1:
        return 1
    # x = floan)
    memo[key] = gridTraveler(m - 1, n,memo) + gridTraveler(m, n - 1,memo)


    return memo[key]


class Solution:

    # def __int__(self):

    memo = {}

    def tribonacci(self, n):
        if n in self.memo:

            return self.memo[n]

        if n == 0:
            return 0

        if n<=2 :
            return 1

        self.memo[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3);
        return self.memo[n]




print(gridTraveler(18, 18))

# print(fib(100))
