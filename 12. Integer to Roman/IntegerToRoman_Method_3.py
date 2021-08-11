class Solution:
    def intToRoman(self, num: int) -> str:
        d = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        res = ""
        for i in d:
            print(i, d[i])
            res += (num // i) * d[i]
            num %= i
        return res

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