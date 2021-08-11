class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1, 
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    
        lenth = len(s)
        if lenth <= 0 or lenth > 15:
            print('Please input correct data!')
        else:
            result = 0
            index = lenth - 1
            comparedLetter = s[index]
            print('init comparedLetter: ' + comparedLetter)
            while index >= 0:
                # get letter from end to begin
                currentLetter = s[index]
                temp = 0
                
                print('comparedLetter: ' + comparedLetter)
                print('currentLetter: ' + currentLetter)
                if currentLetter == comparedLetter:
                    # first time will enter (last digit = last digit)
                    # current == comparedLetter
                    temp = temp + roman[currentLetter]
                    print('------ A ------')
                elif currentLetter != comparedLetter:
                    current = roman[currentLetter]
                    compare = roman[comparedLetter]
                    if current > compare:
                        temp = temp + current
                        comparedLetter = currentLetter
                        print('------ B ------')
                    else:
                        temp = temp - current
                        comparedLetter = currentLetter
                        print('------ C ------')
                # elif roman[currentLetter] > roman[comparedLetter]:
                #     # current > compared, plus
                #     temp = temp + roman[currentLetter]
                #     compareLetter = currentLetter
                #     print('------ B ------')
                # elif roman[currentLetter] < roman[compareLetter]:
                #     # current < compared, minus
                #     temp = temp - roman[currentLetter]
                #     compareLetter = currentLetter
                #     print('------ C ------')
                index = index - 1
                result = result + temp
            return result
                

test = Solution
print('****** Test Case: III ******')
print(test.romanToInt(test, s='III'))
print('****** Test Case END ******\n')
print('****** Test Case: IV ******')
print(test.romanToInt(test, s='IV'))
print('****** Test Case END ******\n')
print('****** Test Case: IX ******')
print(test.romanToInt(test, s='IX'))
print('****** Test Case END ******\n')
print('****** Test Case: LVIII ******')
print(test.romanToInt(test, s='LVIII'))
print('****** Test Case END ******\n')
print('****** Test Case: MCMXCIV ******')
print(test.romanToInt(test, s='MCMXCIV'))
print('****** Test Case END ******\n')