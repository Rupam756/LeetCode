class Solution:
    def maxDepth(self, s: str) -> int:

        current = 0
        max_depth = 0

        # string --> char

        for char in s:
        # check (
         if char == '(':
            current += 1
            max_depth = max(max_depth, current)

         elif char == ')':
            current -= 1

        return max_depth


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna