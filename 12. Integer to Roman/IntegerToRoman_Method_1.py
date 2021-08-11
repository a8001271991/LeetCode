class Solution:
    def intToRoman(self, num: int) -> str:
        ones = ['I', 'X', 'C', 'M']
        fives = ['V', 'L', 'D']
        i = 0
        ans = []

        while num > 0:
            n = num % 10
            if 1 <= n <= 3:
                ans.append(ones[i] * n) 
            elif n == 4:
                ans.append(ones[i] + fives[i])
            elif 5 <= n <= 8:
                ans.append(fives[i] + ones[i] * (n - 5))
            elif n == 9:
                ans.append(ones[i] + ones[i+1])

            i += 1
            num //= 10

        return "".join(ans[::-1])

test = Solution
print('****** Test Case: 3 ******')
assert test.intToRoman(test, num=3) == 'III'
print('****** Test Case END ******\n')
print('****** Test Case: 5 ******')
assert test.intToRoman(test, num=5) == 'V'
print('****** Test Case END ******\n')
print('****** Test Case: 9 ******')
assert test.intToRoman(test, num=9) == 'IX'
print('****** Test Case END ******\n')
print('****** Test Case: 58 ******')
assert test.intToRoman(test, num=58) == 'LVIII'
print('****** Test Case END ******\n')
print('****** Test Case: 1994 ******')
assert test.intToRoman(test, num=1994) == 'MCMXCIV'
print('****** Test Case END ******\n')