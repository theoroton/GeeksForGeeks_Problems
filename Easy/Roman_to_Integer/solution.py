class Solution:
    def romanToDecimal(self, s): 
        # Dictionnary to store the roman symbols and their associated values
        romans_numbers = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        sum = 0
        # For each roman symbol in the string
        for idx in range(len(s)):
            current_symbol = s[idx] # Get the current symbol
            next_symbol = None
            # Get the next symbol (if in string)
            if idx + 1 < len(s):
                next_symbol = s[idx + 1]
            
            # If next symbol present and is higher than current, we reduce the sum by current symbol associated value
            if next_symbol is not None and romans_numbers[current_symbol] < romans_numbers[next_symbol]:
                sum -= romans_numbers[current_symbol]
            else:
                sum += romans_numbers[current_symbol]
        
        return sum