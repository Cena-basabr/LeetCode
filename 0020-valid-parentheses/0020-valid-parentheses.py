class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
                
        return not stack

solver = Solution()


print(f"'()': {solver.isValid('()')}")               # Expected: True
print(f"'()[]{{}}': {solver.isValid('()[]{}')}")     # Expected: True
print(f"'(]': {solver.isValid('(]')}")               # Expected: False
print(f"'([)]': {solver.isValid('([)]')}")           # Expected: False
print(f"'{{[]}}': {solver.isValid('{[]}')}")         # Expected: True
print(f"'[': {solver.isValid('[')}")                 # Expected: False