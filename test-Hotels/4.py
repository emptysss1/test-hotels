class Solution():
    def get_multiplication_table(self: int):
        print('   ', end=' ')
        for i in range(1, self + 1):
            print('{:>2}'.format(i), end=' ')
        k = 1
        while k <= self:
            print('\n', k, end='  ')
            for i in range(1, self + 1):
                print(''.join('{:>2}'.format(str(k*i))), end=' ')
            k += 1


x = Solution
x.get_multiplication_table(int(input()))
