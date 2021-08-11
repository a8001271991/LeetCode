class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ''
        for value in list(address):
            if value == '.':
                result = result + '[.]'
            else:
                result = result + value
        return result

sol = Solution
print(sol.defangIPaddr(sol, address='1.1.1.1'))