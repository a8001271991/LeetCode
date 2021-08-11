class Solution:
    def intToRoman(self, num: int) -> str:
        M=["","M","MM","MMM"]
        C=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        X=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        I=["","I","II","III","IV","V","VI","VII","VIII","IX"]
        
        return M[num//1000]+C[(num//100)%10]+X[(num//10)%10]+I[num%10]

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