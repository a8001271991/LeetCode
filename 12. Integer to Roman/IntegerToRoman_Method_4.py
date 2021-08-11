class Solution:
    def intToRoman(self, num: int) -> str:
        
        vals = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        romans = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        
        res=''
        
        for i,v in enumerate(vals):
            print(i, v, romans[i])
            res += (num//v) * romans[i]
            num %= v
            
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