class Solution:
    def isBalanced(self, s):
        stack = [] # Use a stack to store brackets => first element of Stack is last opened bracket
        opening_brackets = "([{"
        
        for b in s:
            # If bracket is an opening bracket
            if b in opening_brackets:
                stack.append(b) # Add it to stack
            # If bracket is a closing bracket
            else:
                # If no opening bracket in stack => the expression is unbalanced
                if len(stack) == 0:
                    return False
                    
                ob = stack.pop() # Get last opened bracket
                # If closing bracket does not correspond to opening bracket => the expression is unbalanced
                if ((ob == '(' and b != ')') or
                    (ob == '[' and b != ']') or
                    (ob == '{' and b != '}')):
                   return False
        # If stack is empty at the end => the expression is balanced
        if len(stack) == 0:
            return True
        # Else => the expression is unbalanced
        else:
            return False