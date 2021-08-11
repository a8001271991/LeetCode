class Solution:
    def toLowerCase(self, s: str) -> str:
        if len(s) < 1 or len(s) > 100:
            print('Please input correct Data')
            raise Exception('Wrong Data!')
        else:
            result = s.lower()
            return result