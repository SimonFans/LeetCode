class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        absolute_path = ''
        
        char_list = path.split('/')
        
        for char in char_list:
            # Do nothing
            if char == '' or char == '.':
                continue
            # When stack is empty, do nothing
            elif not stack and char == '..':
                continue
            # When stack is not empty, do pop operation
            elif stack and char == '..':
                stack.pop()
            # Else just add the char to the stack
            else:
                stack.append(char)
        # If stack is empty, just return '/'
        if not stack:
            return '/'
        # Concate those chars left in the stack with '/'
        for item in stack:
            absolute_path += '/' + item
        
        return absolute_path
