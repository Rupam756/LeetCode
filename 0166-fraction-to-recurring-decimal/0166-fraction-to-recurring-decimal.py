class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Edge case for zero numerator
        if numerator == 0:
            return "0"
            
        res = []
        
        # Determine the sign (XOR checks if exactly one number is negative)
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")
            
        # Work with absolute values
        num = abs(numerator)
        den = abs(denominator)
        
        # 1. Calculate the integer part
        res.append(str(num // den))
        
        # Calculate the remainder
        rem = num % den
        if rem == 0:
            # If no remainder, we just return the integer part
            return "".join(res)
            
        # 2. Calculate the fractional part
        res.append(".")
        
        # Dictionary to store the remainder and its index in the `res` list
        # This helps us identify where a repeating decimal starts
        rem_map = {}
        
        while rem != 0:
            if rem in rem_map:
                # We have seen this remainder before, meaning the sequence repeats
                res.insert(rem_map[rem], "(")
                res.append(")")
                break
            
            # Store the current length as the index for this remainder
            rem_map[rem] = len(res)
            
            # Multiply remainder by 10 to get the next decimal digit
            rem *= 10
            res.append(str(rem // den))
            rem %= den
            
        return "".join(res)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna